from os import environ
from pathlib import Path

from djmoney.money import Currency

ALLOWED_EMAIL_DOMAINS = ["prefeitura.rio", "rio.rj.gov.br"]
ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", "localhost").split(",")
CSRF_TRUSTED_ORIGINS = environ.get("CSRF_TRUSTED_ORIGINS", "http://localhost:1337").split(",")
BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD_URL = environ.get("DASHBOARD_URL", "http://localhost:8001")
DATE_INPUT_FORMATS = ["%d/%m/%Y", "%d-%m-%Y", "%d %b %Y"]
DEBUG = environ.get("DEBUG", "1") == "1"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DEFAULT_CURRENCY = Currency("BRL")
GRAPH_MODELS = {"app_labels": ["etp", "tr"]}
LANGUAGE_CODE = "pt-BR"
MEDIA_URL = "media/"
OLLAMA_API_URL = environ.get("OLLAMA_API_URL", "http://localhost:8001")
ROOT_URLCONF = "licitacaorio.urls"
SECRET_KEY = environ["SECRET_KEY"]
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "assets"
STATIC_URL = "assets/"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "licitacaorio.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djmoney",
    "users",
    "etp",
    "tr",
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
        "ENGINE": environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": environ.get("DB_USER", None),
        "PASSWORD": environ.get("DB_PASSWORD", None),
        "HOST": environ.get("DB_HOST", None),
        "PORT": environ.get("DB_PORT", None),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
