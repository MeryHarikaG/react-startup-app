
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
# Static files (CSS, JavaScript, images)
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'Frontend' / 'build' / 'static']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=4b!i3z3$m_e=#8f11@anqkqy^we0wtjar!-$na-!cfws8q_1)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['startupclub.onrender.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'Frontend',
    'rest_auth',
    'corsheaders',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # or your local frontend URL
    # 'http://127.0.0.1:3000',
    # 'http://localhost:8000',  # or your local Django development server
    # 'http://127.0.0.1:8000',
    # 'http://localhost:4200',  # for Angular development server, if applicable
    # 'http://127.0.0.1:4200',
    # 'http://localhost:8080',  # for Vue.js development server, if applicable
    # 'http://127.0.0.1:8080',
    # 'http://localhost:8081',  # for React development server, if applicable
    # 'http://127.0.0.1:8081',
    # 'http://localhost:8888',  # for Jupyter notebooks
    # 'http://127.0.0.1:8888',
    # 'http://localhost:8001',  # for Django Debug Toolbar
    # 'http://127.0.0.1:8001',
    # 'http://localhost:5000',  # for Flask development server
    # 'http://127.0.0.1:5000',
    "https://wonderful-sprinkles-775c04.netlify.app",
    # '*',
]
ROOT_URLCONF = 'Backend.urls'

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "build", "static")
    # '../Frontend/build/static',
]
# STATICFILES_DIRS = [
#     BASE_DIR / 'Frontend/build/static',
# ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_EMAIL_REQUIRED = False
# settings.py

# Use the 'django.db.models.AutoField' for Django versions below 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
