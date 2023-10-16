from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render
from django.urls import path, include
from .views import index

# Create your views here.
urlpatterns = [
    path('ws/async/', index),
]
urlpatterns += staticfiles_urlpatterns()
