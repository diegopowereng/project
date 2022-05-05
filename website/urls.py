"""Arquivos urls.py que está em cliente"""
from django.urls import path
from . import views

app_name='website'

urlpatterns = [
    path('', views.index, name='index'),
]