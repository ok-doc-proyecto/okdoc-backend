from django.urls import path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('all-docs', views.AllDocs, 'all-docs')
router.register(
    'doc-reviews/(?P<medico_id>[\d]+)', views.DocReviews, 'doc-reviews')

urlpatterns = [
    path('ws/asyncReviews2/<int:medico_id>/',
         views.DocReviews.asyncDocReviews, name='asyncDocReviews'),
]


urlpatterns += router.urls
a = 9
