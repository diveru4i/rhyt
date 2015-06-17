/* global window, jQuery */
(function ($) {
    'use strict';

    function Form(container, settings) {
        var self = {};
        var $WINDOW = $(window);

        self.id = new Date().getTime();

        self.api = {
            id: self.id
        };

        self.defaults = {
            noValidate: true,
            submitTimeout: 1000,
            showErrors: true,
            fields: 'input:not([type="hidden"]), textarea',
            fieldContainerClassName: 'form-field',
            fieldInUseClassName: 'inuse',
            fieldErrorContainerClassName: 'form-error-text',
            fieldErrorClassName: 'error',
            fieldCaptchaClassName: 'captcha-wrapper img',
            fieldCaptchaRefreshClassName: 'js-captcha-refresh',
            fieldCaptchaRefreshDataUrl: 'refresh-url',
            fieldCaptchaFieldId: 'id_captcha_1',
            fieldCaptchaHiddenFieldId: 'id_captcha_0',
            submitDebounce: true,
            onInit: null,
            onChange: null,
            onReset: null,
            onSubmit: null,
            onError: null
        };

        self.params = $.extend(true, self.defaults, settings);

        self.resetErrorFor = function (name) {
            self.errors[name] = [];
        };

        self.resetErrors = function () {
            self.errors = {
                length: 0
            };
        };

        self.collectErrors = function () {
            self.errors.length = 0;
            var error;
            for (error in self.errors) {
                if (self.errors[error] && self.errors[error].length) {
                    self.errors.length += 1;
                }
            }
            return self.errors.length;
        };

        self.latToCyr = function (latString) {
            var keyboardLat = 'qwertyuiop[{]}asdfghjkl;:\'"\\|`~zxcvbnm,<.>';
            var keyboardCyr = 'йцукенгшщзххъъфывапролджжээёёёёячсмитьббюю';

            return latString.replace(/([a-z;:~,<>\[\{\]\}\'\"\\\.\|])/ig, function (latChar) {
                var cyrChar = keyboardCyr.charAt(keyboardLat.indexOf(latChar.toLowerCase())) || latChar;
                var isUpper = (latChar.toUpperCase() === latChar && latChar.toLowerCase() !== latChar) || /([<>:~\"|\{\}])/ig.test(latChar);
                return isUpper ? cyrChar.toUpperCase() : cyrChar;
            });
        };

        self.busyField = function ($field) {
            $field.closest('.' + self.params.fieldContainerClassName)
                .addClass(self.params.fieldInUseClassName);

            return self;
        };

        self.freeField = function ($field) {
            $field.closest('.' + self.params.fieldContainerClassName)
                .removeClass(self.params.fieldInUseClassName);

            return self;
        };

        self.checkBusyField = function () {
            var field = this;
            var $field = $(field);

            if (field.value.length) {
                self.busyField($field);
            } else {
                self.freeField($field);
            }

            return self;
        };

        self.refreshCaptcha = function () {
            var $captcha = self.$form.find('.' + self.params.fieldCaptchaClassName);
            var $captchaHiddenField = self.$form.find('#' + self.params.fieldCaptchaHiddenFieldId);
            var $captchaField = self.$form.find('#' + self.params.fieldCaptchaFieldId);
            var refreshUrl = self.$captchaBtn.data(self.params.fieldCaptchaRefreshDataUrl) || '';
            if ($captcha.length) {
                $.ajax({
                    url: refreshUrl,
                    type: 'get',
                    dataType: 'json',
                    success: function (json) {
                        if (json.new_cptch_key && json.new_cptch_image) {
                            $captchaHiddenField.val(json.new_cptch_key);
                            $captchaField.val('');
                            $captcha.attr('src', json.new_cptch_image);
                        }
                    }
                });
            }
        };

        self.clearField = function () {
            var field = this;
            var $field = $(field);
            if (!$field.is(':hidden')) {
                $field.val('');
            }
        };

        self.setError = function (fieldName, message) {
            if (!self.errors[fieldName]) {
                self.errors[fieldName] = [message];
            } else {
                self.errors[fieldName].push(message);
            }

            return self;
        };

        self.showErrors = function () {
            self.$fields.each(function () {
                var field = this;
                var $field = $(field);
                var $fieldContainer = $field.closest('.' + self.params.fieldContainerClassName);
                var $fieldErrorContainer = $fieldContainer.find('.' + self.params.fieldErrorContainerClassName);

                if (self.errors[field.name] && self.errors[field.name].length) {
                    $fieldContainer.addClass(self.params.fieldErrorClassName);
                    if (self.params.showErrors && self.errors) {
                        $fieldErrorContainer.text(self.errors[field.name][0]);
                    }
                } else {
                    $fieldContainer.removeClass(self.params.fieldErrorClassName);
                }
            });
        };

        self.modifyField = function (e) {
            var field = this;
            var classes = this.className;
            var value = field.value;
            var trimValue = $.trim(value);

            if (classes.indexOf('to-cyrillic') > -1) {
                if (trimValue.length) {
                    var cyrValue = self.latToCyr(value);
                    if (cyrValue !== value) {
                        field.value = cyrValue;
                    }
                }
            }
        };

        self.validateField = function () {
            var field = this;
            var classes = this.className;
            var value = $.trim(field.value);

            self.resetErrorFor(field.name);

            if (classes.indexOf('is-required') > -1 || field.required === true) {
                if (!value.length) {
                    self.setError(field.name, 'Обязательное поле');
                }
            }

            if (classes.indexOf('is-name') > -1) {
                if (!new RegExp('^([a-zа-яё]{1})([a-zа-яё0-9 .,;:"\/\\\\)(_«»<>“”-]{2,254})$', 'ig').test(value)) {
                    self.setError(field.name, 'Недопустимое значение');
                }
            }

            if (classes.indexOf('is-email') > -1 || field.type === 'email') {
                if (!new RegExp('^[a-z0-9](([\'_.-]?[a-z0-9]+)*)[@]([a-z0-9]+)(([.-]?[a-z0-9]+)*)[.]([a-z]{2,})([ ]+)?$', 'i').test(value)) {
                    self.setError(field.name, 'Недопустимое значение');
                }
            }

            if (classes.indexOf('is-message') > -1) {
                if (!new RegExp('^(.{1,10000})', 'g').test(value)) {
                    self.setError(field.name, 'Недопустимое значение');
                }
            }

            if (classes.indexOf('is-captcha') > -1) {
                if (!new RegExp('^([a-z]{6})$', 'ig').test(value)) {
                    self.setError(field.name, 'Код введен неверно');
                }
            }

            self.showErrors();
            self.collectErrors();
        };

        self.bindEvents = function () {
            // добавление фокус класса на враппер
            self.$fields.on('keyup change focusout focusin input', self.checkBusyField);
            self.$fields.on('keyup', self.modifyField);
            self.$fields.on('keyup focusout', self.validateField);

            $WINDOW.on('load initForm', function () {
                self.$fields.each(self.checkBusyField);
            }).triggerHandler('initForm');

            // проверка перед отправкой
            self.$form.on('submit', function (e) {
                if (!self.submitted) {
                    if (self.params.submitDebounce) {
                        self.submitted = true;
                        setTimeout(function () {
                            self.submitted = false;
                        }, typeof self.params.submitTimeout === 'number' ? self.params.submitTimeout : self.defaults.submitTimeout);
                    }
                    self.resetErrors();
                    self.$fields.each(self.validateField);
                    if (self.collectErrors()) {
                        e.preventDefault();
                        self.submitted = false;
                        self.showErrors();
                    } else {
                        if ($.isFunction(self.params.onSubmit)) {
                            self.params.onSubmit.call(self, e);
                        }
                    }
                } else {
                    e.preventDefault();
                }
            });

            self.$form.on('reset', function (e) {
                e.preventDefault();
                self.submitted = false;
                self.resetErrors();
                self.refreshCaptcha();
                self.$fields.each(self.clearField);
                self.$fields.each(self.checkBusyField);
                if ($.isFunction(self.params.onReset)) {
                    self.params.onReset.call(self, e);
                }
            });

            self.$form.on('error', function (e, error) {
                self.submitted = false;
                if ($.isFunction(self.params.onError)) {
                    self.params.onError.call(self, e, error);
                }
            });

            self.$form.on('change', function (e) {
                if ($.isFunction(self.params.onChange)) {
                    self.params.onChange.call(self, e);
                }
            });

            // рефреш капчи
            self.$captchaBtn.on('click', function (e) {
                e.preventDefault();
                this.blur();
                self.refreshCaptcha();
            });

        };

        self.init = (function () {
            self.form = container;
            self.$form = $(self.form);

            if (self.params.noValidate) {
                self.$form.attr('novalidate', 'novalidate');
            }

            self.$fields = self.$form.find(self.params.fields);

            self.$captchaBtn = self.$form.find('.' + self.params.fieldCaptchaRefreshClassName);

            self.resetErrors();

            self.bindEvents();

            if ($.isFunction(self.params.onInit)) {
                self.params.onInit.call(self);
            }

            return self;
        }());

        return self.api;
    }

    $.fn.form = function form(settings) {
        return $(this).each(function () {
            if (!$.data(this, 'form')) {
                $.data(this, 'form', new Form(this, settings));
            }
        });
    };

    $.fn.callFormMethod = function callFormMethod(method, params) {
        return $(this).each(function () {
            var form = $.data(this, 'form');
            if (form && $.isFunction(form[method])) {
                form[method](params);
            }
        });
    };
}(jQuery));

//# sourceMappingURL=form.js.map