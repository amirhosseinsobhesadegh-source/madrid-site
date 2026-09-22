"""
تنظیمات اصلی پروژه جنگو.
اینجا محلی هست که پروژه سراسری تنظیم می‌شه (نه یک صفحه به‌خصوص).
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# قبل از بردن سایت روی سرور، این کلید رو با یه متن تصادفی طولانی عوض کن.
SECRET_KEY = "django-insecure-CHANGE-ME-before-deploy"

# روی کامپیوتر خودت True بذار. روی سرور واقعی حتماً False کن.
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

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

# عکس‌ها و فایل‌هایی که کاربر آپلود می‌کنه اینجا ذخیره می‌شن
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
