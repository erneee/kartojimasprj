from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage-url'),
    path('artistai/', views.visi_artistai, name='artistai-visi-url')

]