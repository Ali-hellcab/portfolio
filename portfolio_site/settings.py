"""
Django settings for portfolio_site project.
──────────────────────────────────────────
Fill in the sections marked with  ← YOUR ...  before deploying.
"""

from pathlib import Path
import os

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent


# ── Security ──────────────────────────────────────────────────────────────────
# ← YOUR secret key (generate with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-key-change-in-production')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']  # We'll tighten this on PythonAnywhere


# ── Installed Apps ────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    # "whitenoise.runserver_nostatic",  # ← Uncomment for production static file serving

    # Local
    "portfolio",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",  # ← Uncomment for production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # Project-level templates directory
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

WSGI_APPLICATION = "portfolio_site.wsgi.application"


# ── Database ──────────────────────────────────────────────────────────────────
# Default: SQLite (fine for personal portfolio)
# For PostgreSQL, replace with:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("DB_NAME", "portfolio_db"),
#         "USER": os.environ.get("DB_USER", "postgres"),
#         "PASSWORD": os.environ.get("DB_PASSWORD", ""),
#         "HOST": os.environ.get("DB_HOST", "localhost"),
#         "PORT": os.environ.get("DB_PORT", "5432"),
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ── Static Files ──────────────────────────────────────────────────────────────
STATIC_URL  = "/static/"
STATIC_ROOT = BASE_DIR / "static_root"   # collectstatic target for production
STATICFILES_DIRS = [
    BASE_DIR / "portfolio" / "static",
]

# WhiteNoise compressed static files (production)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ── Media Files (uploaded images) ─────────────────────────────────────────────
MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ── Email (contact form) ──────────────────────────────────────────────────────
# ← Replace with your SMTP credentials
EMAIL_BACKEND       = "django.core.mail.backends.console.EmailBackend"  # Prints to console in dev
# EMAIL_BACKEND     = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST        = "smtp.gmail.com"
# EMAIL_PORT        = 587
# EMAIL_USE_TLS     = True
# EMAIL_HOST_USER   = os.environ.get("EMAIL_USER", "")
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS", "")
DEFAULT_FROM_EMAIL  = "portfolio@example.com"     # ← YOUR sender email
CONTACT_EMAIL       = "you@example.com"           # ← YOUR receiving email


# ── Auth & Misc ───────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE     = "UTC"
USE_I18N      = True
USE_TZ        = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
