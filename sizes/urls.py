from django.urls import path
from . import views

urlpatterns = [
    path('', views.mchk_01, name='mchk_01'),
    path('imgident/', views.imgident, name='imgident'),
    path('imgident/translate/', views.translate, name='translate'),
]
