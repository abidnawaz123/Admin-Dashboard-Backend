from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSignupSerializer

class UserSignupView(CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]
