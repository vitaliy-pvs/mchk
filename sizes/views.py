import os

from django.shortcuts import render

from mchk.settings import STATIC_ROOT

STATIC_ROOT = STATIC_ROOT.replace("\\", "/")

favicon_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'favicon.png')):
    favicon_exists = True

logo_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'logo.png')):
    logo_exists = True

header_img_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'header.jpg')):
    header_img_exists = True

page_title_list = [
    ["МШК-01", "mchk_01"],
    ["МШК-01.ОС", "mchk_01_OS"],
    ["МШК-04", "mchk_04"],
    ["МШК-04.ОС", "mchk_04_OS"],
]


def mchk_01(request):
    current_page_title = "МШК-01"
    return render(request, 'mchk_01.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def mchk_01_OS(request):
    current_page_title = "МШК-01.ОС"
    return render(request, 'mchk_01_OS.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def mchk_04(request):
    current_page_title = "МШК-04"
    return render(request, 'mchk_04.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def mchk_04_OS(request):
    current_page_title = "МШК-04.ОС"
    return render(request, 'mchk_04_OS.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })