//===========================
// Обслуживание формы обратной связи
//===========================
    $('.js-feedback-form').form({
        onInit: function () {
            var self = this;
            var $form = self.$form;
            var $formContainer = $form.parent();
            var $toggleReset = $formContainer.find('.js-show-form-reset');
            var $toggle = $formContainer.find('.js-show-form');
            $toggleReset.on('click', function (e) {
                e.preventDefault();
                $formContainer.removeClass('is-processing')
                    .removeClass('is-submitted');
                $form.get(0).reset();
            });
            $toggle.on('click', function (e) {
                e.preventDefault();
                $formContainer.removeClass('is-processing')
                    .removeClass('is-not-submitted');
                self.refreshCaptcha();
            });
        },
        onSubmit: function (e) {
            e.preventDefault();
            var self = this;
            var $form = self.$form;
            var $formContainer = $form.parent();
            var formData = $form.serialize();
            var submitUrl = $form.attr('action');
            var submitType = $form.attr('method');
            $formContainer.addClass('is-processing');
            $.ajax({
                url: submitUrl,
                type: submitType,
                data: formData,
                dataType: 'json',
                success: function (json) {
                    if (json.success === true) {
                        $formContainer.removeClass('is-processing')
                            .addClass('is-submitted');
                    } else {
                        $formContainer.removeClass('is-processing');
                        self.setError('captcha_1', 'Код введен неверно');
                        self.showErrors();
                    }
                },
                error: function (error) {
                    $form.trigger('error', error);
                }
            });
        },
        onError: function (e, error) {
            var self = this;
            var $form = self.$form;
            var $formContainer = $form.parent();
            $formContainer.removeClass('is-processing')
                .addClass('is-not-submitted');
        }
    });
