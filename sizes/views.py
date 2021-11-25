from django.shortcuts import render
from mchk.settings import STATIC_ROOT
from deep_translator import GoogleTranslator
from django.http import JsonResponse

STATIC_ROOT = STATIC_ROOT.replace("\\", "/")

page_title_list = [
    ["МШК-01", "art01"],
    ["МШК-04", "art04"],
    ["МШК-06", "art06"],
    # ["МШК-01", "mchk_01"],
    # ["imgident", "imgident"],
    # ["textident", "textident"],
]


def mchk_01(request):
    current_page_title = "МШК-01"
    return render(request, 'mchk_01.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def art01(request):
    current_page_title = "МШК-01"
    return render(request, 'art01.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def art04(request):
    current_page_title = "МШК-04"
    return render(request, 'art04.html', {
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
