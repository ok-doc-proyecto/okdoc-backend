from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login, name='login'), 
    path('docprofile/', views.docprofile, name='docprofile'), 
    path('userprofile/', views.userprofile, name='userprofile'), 
    path('all-docs/', views.AllDocsList.as_view()),
    path('search/', views.Search.as_view(), name='search'),
    path('review/<int:medico_id>/', views.DocReviewList.as_view(), name='docprofile'),
    path('review/<int:medico_id>/<int:score>/', views.DocReviewList.as_view(), name='docprofile-reviews')
]