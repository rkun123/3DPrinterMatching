from django.urls import path, include
from . import views
from rest_framework import routers, urls

urlpatterns = [
  path('', include('rest_framework.urls', namespace='rest_framework'))
]