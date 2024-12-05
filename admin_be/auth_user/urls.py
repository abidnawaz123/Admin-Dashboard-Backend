from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserSignupView
from .export_as_excel import export_users_xlsx

urlpatterns = [
    path('signup/',UserSignupView.as_view(), name='signup'),
    path('login/',TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token Refresh
    path('export-users/', export_users_xlsx, name='export_users_xlsx'),
]