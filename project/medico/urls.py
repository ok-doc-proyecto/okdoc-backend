from django.urls import path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('all-docs', views.AllDocs, 'all-docs')
router.register('doc-reviews/(?P<medico_id>[\d]+)', views.DocReviews, 'doc-reviews')

urlpatterns = [
]

urlpatterns += router.urls
