"""foods_and_delicacies App URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name='foods_and_delicacies')
]