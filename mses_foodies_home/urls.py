"""Mses_Foodies_home App URL Configuration
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mses_foodies_home'),
]