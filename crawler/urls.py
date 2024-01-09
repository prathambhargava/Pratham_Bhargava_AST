# Crawler/urls.py
from django.urls import path
from .views import job_search

urlpatterns = [
    path('job-search/', job_search, name='job_search'),
    path('', job_search, name='job_search'),
]