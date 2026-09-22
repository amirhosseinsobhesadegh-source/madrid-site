"""
نقشه اصلی آدرس‌های سایت.
هر آدرسی که کاربر توی مرورگر باز می‌کنه، از اینجا مسیر می‌شه.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  # پنل مدیریت آماده خود جنگو
    path("", include("info.urls")),   # بقیه آدرس‌ها رو به اپ info می‌سپاریم
]

# فقط روی کامپیوتر خودت (DEBUG=True) عکس‌های آپلودشده رو مستقیم نشون بده
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
