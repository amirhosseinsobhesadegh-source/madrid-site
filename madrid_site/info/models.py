"""
«مدل» یعنی جنگو خودش یه جدول توی دیتابیس برامون می‌سازه.
هر ردیف این جدول، یک عکس آپلودشده رو نشون می‌ده.
"""

from django.db import models


class Photo(models.Model):
    title = models.CharField("عنوان", max_length=100, blank=True)
    image = models.ImageField("عکس", upload_to="photos/")
    uploaded_at = models.DateTimeField("تاریخ آپلود", auto_now_add=True)

    def __str__(self):
        return self.title or f"عکس شماره {self.pk}"

    class Meta:
        ordering = ["-uploaded_at"]
