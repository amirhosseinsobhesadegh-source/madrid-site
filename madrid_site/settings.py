"""
تنظیمات اصلی پروژه جنگو.
اینجا محلی هست که پروژه سراسری تنظیم می‌شه (نه یک صفحه به‌خصوص).
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# روی سرور، این مقدار رو از یه متغیر محیطی به اسم SECRET_KEY می‌خونه.
# روی کامپیوتر خودت (وقتی اون متغیر رو تنظیم نکردی)، از همین مقدار پیش‌فرض استفاده می‌کنه.
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-CHANGE-ME-before-deploy")

# روی کامپیوتر خودت True می‌مونه. روی سرور، متغیر محیطی DEBUG=False رو تنظیم می‌کنیم.
DEBUG = os.environ.get("DEBUG", "True") == "True"

# روی سرور، آدرس سایتت رو با متغیر محیطی ALLOWED_HOSTS مشخص می‌کنیم (با کاما جدا اگه چندتا بود).
_hosts = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost")
ALLOWED_HOSTS = [h.strip() for h in _hosts.split(",") if h.strip()]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "info",  # اپلیکیشن خودمون
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # فایل‌های استاتیک رو روی سرور سرو می‌کنه
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "madrid_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,  # یعنی جنگو خودش پوشه templates هر اپ رو پیدا می‌کنه
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

WSGI_APPLICATION = "madrid_site.wsgi.application"

# دیتابیس پیش‌فرض: یک فایل ساده SQLite کنار پروژه
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # جایی که collectstatic فایل‌ها رو جمع می‌کنه
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# عکس‌ها و فایل‌هایی که کاربر آپلود می‌کنه اینجا ذخیره می‌شن
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
