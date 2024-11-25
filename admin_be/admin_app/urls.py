from django.contrib import admin
from django.urls import path,include
from .views import LatestCustomersView
from .user_auth.urls import urlpatterns as up

urlpatterns = [
    path('latest_customers/',LatestCustomersView.as_view(),name='latest_customers'),
]

urlpatterns += up
