"""
Django settings for kwikemart project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q%_abn%u8v-qh5b)l*+u&&og+5goq27(d@qdsz^r+c)49r9v07"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STRIPE_PUB_KEY='pk_test_51O2HRpDh5kW7ZhzSeIgdg2TqdBSjmkmu1KImdwZrNHzdUnUmzROshTeJr090oGquZ70CRF94Cx6LCWZOg6YTtWjW00L7JVBRXe'
STRIPE_SECRET_KEY='sk_test_51O2HRpDh5kW7ZhzSqzPCf0Xv1fBqS2iQs3mwfCIo70TsAZrItCn1ZZdx7YvJHVHHsOL8cCc9UNmgwfcYw9UswJZ300pC1UclIU'


ALLOWED_HOSTS = []

LOGIN_URL='login'
LOGIN_REDIRECT_URL='vendor_admin'
LOGOUT_REDIRECT_URL='frontpage'

SESSION_COOKIE_AGE=86400
CART_SESSION_ID='cart'

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.vendor",
    "apps.core",
    "apps.product"
    
    
    
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "kwikemart.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.product.context_processors.menu_categories",
                "apps.cart.context_processors.cart"
            ],
        },
    },
]

WSGI_APPLICATION = "kwikemart.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS=[
    BASE_DIR / 'static'
]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media/'







# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
