from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login, name='login'), 
    path('docprofile/', views.docprofile, name='docprofile'), 
    path('userprofile/', views.userprofile, name='userprofile'), 
    path('all-docs/', views.AllDocsList.as_view()),
]