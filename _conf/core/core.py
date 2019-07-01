# -*- coding: utf-8 -*-
import os


SITE_ID = 1
SECRET_KEY = 'kvdd=hcmg(=xe4mr+5&pin-ax)m*z+#f#)v)o%cu@$@-n@2r9e'

ADMINS = (
    ('Melfi Silver', 'webmaster@designdepot.ru'),
)

MANAGERS = ADMINS


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

FILE_UPLOAD_PERMISSIONS = 0o644

YOUTUBE_COVERS_ROOT = os.path.join(MEDIA_ROOT, 'covers')
YOUTUBE_COVERS_MEDIA = '/media/covers/'
YOUTUBE_API_KEY = 'AIzaSyClQXA4Mxic0itXGegC8Y18T6QvePy4B2I'


# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Moscow'

LANGUAGES = [
    ('ru', u'Русский'),
    # ('en', u'Английский'),
]

LANGUAGE_CODE = LANGUAGES[0][0]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

    'core.middleware.set_config',

    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

EXCLUDE_FROM_MINIFYING = ['^admin/']

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
            os.path.join(PROJECT_ROOT, 'markup'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                'core.context_processors.set_stuff',
            ],
            'debug': True,
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'taggit',
    'compressor',
    'modelcluster',
    'gunicorn',
    'captcha',
    'imperavi',
    'easy_thumbnails',
    'el_pagination',

    'wagtail.core',
    'wagtail.admin',
    'wagtail.search',
    'wagtail.images',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.sites',
    'wagtail.embeds',
    'wagtail.contrib.redirects',
    # 'wagtail.forms',

    'wagtail.contrib.styleguide',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.sitemaps',

    'core',
]


TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        # 'core': {
        #     'level': 'INFO',
        #     'class': 'logging.FileHandler',
        #     'filename': os.path.join(PROJECT_ROOT, 'log', 'core.log'),
        #     'formatter': 'verbose',

        # }
    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'sent_emails': {
        #     'handlers': ['core'],
        #     'level': 'INFO',
        # }
    }
}
