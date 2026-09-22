"""
اینجا جایی‌ه که برای هر صفحه، داده‌ها رو آماده می‌کنی و به قالب HTML می‌فرستی.
معادل مستقیم چیزی‌ه که توی نسخه Flask زیر @app.route می‌نوشتیم.
"""

from django.shortcuts import redirect, render

from .forms import PhotoUploadForm
from .models import Photo

CLUB_FACTS = {
    "نام کامل": "رئال مادرید کلوب دو فوتبال",
    "سال تأسیس": "۱۹۰۲",
    "ورزشگاه": "سانتیاگو برنابئو",
    "شهر": "مادرید، اسپانیا",
    "رنگ پیراهن": "سفید",
    "لقب‌ها": "لوس بلانکوس، لا فابریکا (آکادمی)",
}

BARCA_FACTS = {
    "نام کامل": "فوتبال کلوب بارسلونا",
    "سال تأسیس": "۱۸۹۹",
    "ورزشگاه": "اسپاتیفای کمپ‌نو",
    "شهر": "بارسلونا، اسپانیا",
    "رنگ پیراهن": "آبی و قرمز (بلاگرانا)",
    "لقب‌ها": "بارسا، کولبلوگرانا",
}

RECENT_RESULTS = [
    {"date": "۳۰ شهریور ۱۴۰۵", "home": "اسپانیول", "away": "رئال مادرید", "score": "۱ - ۲"},
    {"date": "۴ شهریور ۱۴۰۵", "home": "رئال مادرید", "away": "رئال سوسیداد", "score": "۴ - ۱"},
    {"date": "۸ شهریور ۱۴۰۵", "home": "رئال مادرید", "away": "مالاگا", "score": "۴ - ۰"},
    {"date": "۱۳ شهریور ۱۴۰۵", "home": "رئال بتیس", "away": "رئال مادرید", "score": "۱ - ۰"},
    {"date": "۲۱ شهریور ۱۴۰۵", "home": "رئال مادرید", "away": "رایو وایکانو", "score": "۴ - ۱"},
    {"date": "۲۴ شهریور ۱۴۰۵", "home": "الچه", "away": "رئال مادرید", "score": "۳ - ۲"},
    {"date": "۲۹ شهریور ۱۴۰۵", "home": "اتلتیکو مادرید", "away": "رئال مادرید", "score": "۲ - ۱"},
]

UPCOMING_FIXTURES = [
    {"date": "۱۸ مهر ۱۴۰۵", "home": "رئال مادرید", "away": "ویارئال"},
    {"date": "۲۶ مهر ۱۴۰۵", "home": "رئال مادرید", "away": "سویا"},
    {"date": "۳ آبان ۱۴۰۵", "home": "بارسلونا", "away": "رئال مادرید"},
    {"date": "۱۰ آبان ۱۴۰۵", "home": "راسینگ سانتاندر", "away": "رئال مادرید"},
    {"date": "۱۷ آبان ۱۴۰۵", "home": "والنسیا", "away": "رئال مادرید"},
]

BARCA_RECENT_RESULTS = [
    {"date": "۹ شهریور ۱۴۰۵", "home": "بارسلونا", "away": "رایو وایکانو", "score": "۵ - ۲"},
    {"date": "۱۵ شهریور ۱۴۰۵", "home": "والنسیا", "away": "بارسلونا", "score": "۰ - ۵"},
    {"date": "۲۲ شهریور ۱۴۰۵", "home": "لوانته", "away": "بارسلونا", "score": "۲ - ۴"},
    {"date": "۲۵ شهریور ۱۴۰۵", "home": "بارسلونا", "away": "راسینگ سانتاندر", "score": "۷ - ۲"},
    {"date": "۲۸ شهریور ۱۴۰۵", "home": "سویا", "away": "بارسلونا", "score": "۱ - ۳"},
]

BARCA_UPCOMING_FIXTURES = [
    {"date": "۱۸ مهر ۱۴۰۵", "home": "بارسلونا", "away": "ختافه"},
    {"date": "۲۵ مهر ۱۴۰۵", "home": "رئال بتیس", "away": "بارسلونا"},
    {"date": "۳ آبان ۱۴۰۵", "home": "بارسلونا", "away": "رئال مادرید"},
    {"date": "۱۰ آبان ۱۴۰۵", "home": "بارسلونا", "away": "دپورتیوو آلاوس"},
    {"date": "۱۷ آبان ۱۴۰۵", "home": "اتلتیکو مادرید", "away": "بارسلونا"},
]

LALIGA_TABLE = [
    {"rank": 1, "team": "بارسلونا", "w": 7, "d": 0, "l": 0, "pts": 21},
    {"rank": 2, "team": "اتلتیکو مادرید", "w": 5, "d": 1, "l": 1, "pts": 16},
    {"rank": 3, "team": "رئال بتیس", "w": 5, "d": 1, "l": 1, "pts": 16},
    {"rank": 4, "team": "رئال مادرید", "w": 5, "d": 0, "l": 2, "pts": 15},
    {"rank": 5, "team": "سویا", "w": 4, "d": 1, "l": 2, "pts": 13},
    {"rank": 6, "team": "دپورتیوو آلاوس", "w": 3, "d": 2, "l": 2, "pts": 11},
    {"rank": 7, "team": "دپورتیوو لاکرونیا", "w": 2, "d": 4, "l": 1, "pts": 10},
    {"rank": 8, "team": "رئال سوسیداد", "w": 3, "d": 1, "l": 3, "pts": 10},
    {"rank": 9, "team": "ویارئال", "w": 2, "d": 2, "l": 3, "pts": 8},
    {"rank": 10, "team": "اتلتیک بیلبائو", "w": 2, "d": 2, "l": 2, "pts": 8},
    {"rank": 11, "team": "ختافه", "w": 2, "d": 2, "l": 3, "pts": 8},
    {"rank": 12, "team": "رایو وایکانو", "w": 2, "d": 2, "l": 3, "pts": 8},
    {"rank": 13, "team": "اوساسونا", "w": 2, "d": 2, "l": 3, "pts": 8},
    {"rank": 14, "team": "سلتاویگو", "w": 1, "d": 4, "l": 2, "pts": 7},
    {"rank": 15, "team": "اسپانیول", "w": 2, "d": 1, "l": 4, "pts": 7},
    {"rank": 16, "team": "راسینگ سانتاندر", "w": 2, "d": 1, "l": 4, "pts": 7},
    {"rank": 17, "team": "لوانته", "w": 1, "d": 2, "l": 3, "pts": 5},
    {"rank": 18, "team": "الچه", "w": 1, "d": 2, "l": 4, "pts": 5},
    {"rank": 19, "team": "والنسیا", "w": 1, "d": 1, "l": 5, "pts": 4},
    {"rank": 20, "team": "مالاگا", "w": 0, "d": 3, "l": 4, "pts": 3},
]

RMA_LINEUP = [
    {"name": "تیبو کورتوا", "pos": "دروازه‌بان"},
    {"name": "دنزل دامفریز", "pos": "مدافع"},
    {"name": "ایبراهیما کوناته", "pos": "مدافع"},
    {"name": "دین هویسن", "pos": "مدافع"},
    {"name": "مارک کوکورویا", "pos": "مدافع"},
    {"name": "فدریکو والورده", "pos": "هافبک"},
    {"name": "اورلین چوامنی", "pos": "هافبک"},
    {"name": "آردا گولر", "pos": "مهاجم"},
    {"name": "جود بلینگام", "pos": "هافبک"},
    {"name": "وینیسیوس جونیور", "pos": "مهاجم"},
    {"name": "کیلیان امباپه", "pos": "مهاجم"},
]

BARCA_LINEUP = [
    {"name": "دومینیک لیواکوویچ", "pos": "دروازه‌بان"},
    {"name": "اریک گارسیا", "pos": "مدافع"},
    {"name": "پائو کوبارسی", "pos": "مدافع"},
    {"name": "آندریاس کریستنسن", "pos": "مدافع"},
    {"name": "ژوآئو کانسلو", "pos": "مدافع"},
    {"name": "پدری", "pos": "هافبک"},
    {"name": "رودری", "pos": "هافبک"},
    {"name": "فرمین لوپز", "pos": "هافبک"},
    {"name": "لامین یامال", "pos": "مهاجم"},
    {"name": "رافینیا", "pos": "مهاجم"},
    {"name": "آنتونی گوردون", "pos": "مهاجم"},
]


def home(request):
    """صفحه اصلی سایت. این تابع همون کاری رو می‌کنه که توی Flask تابع زیر @app.route('/') می‌کرد."""
    context = {
        "facts": CLUB_FACTS,
        "results": RECENT_RESULTS,
        "fixtures": UPCOMING_FIXTURES,
        "barca_facts": BARCA_FACTS,
        "barca_results": BARCA_RECENT_RESULTS,
        "barca_fixtures": BARCA_UPCOMING_FIXTURES,
        "rma_lineup": RMA_LINEUP,
        "barca_lineup": BARCA_LINEUP,
        "table": LALIGA_TABLE,
    }
    return render(request, "info/home.html", context)


def gallery(request):
    """صفحه آپلود و نمایش عکس‌ها."""
    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gallery")  # بعد از آپلود، همین صفحه رو دوباره باز کن
    else:
        form = PhotoUploadForm()

    photos = Photo.objects.all()
    return render(request, "info/gallery.html", {"form": form, "photos": photos})
