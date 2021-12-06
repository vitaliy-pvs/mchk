from django.urls import path
from . import views

urlpatterns = [

    path('', views.art01, name='art01'),
    path('art04/', views.art04, name='art04'),
    path('art06/', views.art06, name='art06'),
    path('mchk_01/', views.mchk_01, name='mchk_01'),
    path('imgident/', views.imgident, name='imgident'),
    path('textident/', views.textident, name='textident'),
    path('imgident/translate/', views.translate, name='translate'),
]
