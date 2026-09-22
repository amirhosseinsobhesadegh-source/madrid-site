"""فایلی که سرورهای تولیدی (مثل gunicorn) برای اجرای سایت به‌کار می‌برن."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "madrid_site.settings")

application = get_wsgi_application()
