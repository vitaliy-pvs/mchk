import os
from django.shortcuts import render
from mchk.settings import STATIC_ROOT
from deep_translator import GoogleTranslator
from django.http import JsonResponse

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
    ["МШК-06", "art06"],
    ["МШК-01", "mchk_01"],
    ["imgident", "imgident"],
    ["textident", "textident"],
]


def mchk_01(request):
    current_page_title = "МШК-01"
    return render(request, 'mchk_01.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def art06(request):
    current_page_title = "МШК-06"
    return render(request, 'art06.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def imgident(request):
    current_page_title = "imgident"
    return render(request, 'imgident.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def translate(request):
    response = {
        'translate_str': GoogleTranslator(source='en', target='ru').translate(request.GET.get('text', None))
    }
    return JsonResponse(response)


def textident(request):
    current_page_title = "textident"
    return render(request, 'textident.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })