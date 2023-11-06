from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render
from django.urls import path, include
from .views import index, asyncDocReviews
from rest_framework import routers

# Create your views here.


urlpatterns = [
    path('ws/async/', index),
    path('ws/asyncReviews/<int:medico>/',
         asyncDocReviews, name='asyncDocReviews'),

]

urlpatterns += staticfiles_urlpatterns()
