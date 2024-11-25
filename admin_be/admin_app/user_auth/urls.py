from django.urls import path
from .views import Signup_view, Login_view

urlpatterns = [
        path('login/',Login_view.as_view(), name='login'),
        path('signup/',Signup_view.as_view(),name='signup'),
    ]