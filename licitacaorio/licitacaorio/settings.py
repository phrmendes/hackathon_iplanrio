from os import environ
from pathlib import Path

from djmoney.money import Currency

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "pt-BR"
MEDIA_URL = "media/"
ROOT_URLCONF = "licitacaorio.urls"
SECRET_KEY = environ["SECRET_KEY"]
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "assets"
STATIC_URL = "static/"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "licitacaorio.wsgi.application"
DEFAULT_CURRENCY = Currency("BRL")
DATE_INPUT_FORMATS = ["%d/%m/%Y", "%d-%m-%Y", "%d %b %Y"]
ALLOWED_EMAIL_DOMAINS = [
    "prefeitura.rio",
    "rio.rj.gov.br",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "djmoney",
    "users",
    "etp",
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


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ["DB_NAME"],
        "USER": environ["DB_USER"],
        "PASSWORD": environ["DB_PASSWORD"],
        "HOST": environ["DB_HOST"],
        "PORT": environ["DB_PORT"],
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

GRAPH_MODELS = {
    "app_labels": ["etp"],
}
