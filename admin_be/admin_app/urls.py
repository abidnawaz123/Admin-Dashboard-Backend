from django.contrib import admin
from django.urls import path,include
from .views import LatestCustomersView
urlpatterns = [
    path('latest_customers/',LatestCustomersView.as_view(),name='latest_customers'),
]
