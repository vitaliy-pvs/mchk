from django.urls import path
from . import views

urlpatterns = [
    path('', views.mchk_01, name='mchk_01'),
    # path('mchk_01_OS', views.mchk_01_OS, name='mchk_01_OS'),
    # path('mchk_04', views.mchk_04, name='mchk_04'),
    # path('mchk_04_OS', views.mchk_04_OS, name='mchk_04_OS'),

    # path('pagelist/<int:pk>/', views.page_list, name='page_list'),
    # path('page/<int:pk>/', views.page, name='page'),
    # path('menu/<int:pk>/', views.menu_page, name='menu_page'),
]
