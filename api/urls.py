from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import PingView

urlpatterns = [
    path('ping/', PingView.as_view()),
]
