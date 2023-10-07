from django.shortcuts import render
from django.urls import path, include
from .views import index

# Create your views here.
urlpatterns = [
    path('functionServices/', index),   
]
