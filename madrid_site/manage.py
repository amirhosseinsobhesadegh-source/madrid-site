#!/usr/bin/env python
"""ابزار خط‌فرمان جنگو. تقریباً همیشه با همین فایل کارها رو اجرا می‌کنی."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "madrid_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "جنگو نصب نیست یا محیط مجازی فعال نیست. "
            "دستور 'pip install django' رو بزن و مطمئن شو (venv) فعاله."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
