from django.urls import path
from .views import LatestCustomersView

urlpatterns = [
    path('latest_customers/',LatestCustomersView.as_view(),name='latest_customers'),
]
