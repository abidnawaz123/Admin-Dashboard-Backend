from django.urls import path
from .views import LatestCustomersView,StudentRecordView

urlpatterns = [
    path('latest_customers/',LatestCustomersView.as_view(),name='latest_customers'),
    path('student/',StudentRecordView.as_view(),name="students")
]
