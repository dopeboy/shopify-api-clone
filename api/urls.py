from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import PingView

urlpatterns = [
    path('ping/', PingView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('stores/', views.StoreList.as_view()),
    path('stores/<int:pk>', views.StoreDetail.as_view()),
    path('purchases/', views.PurchaseList.as_view()),
    path('purchases/<int:pk>', views.PurchaseDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)