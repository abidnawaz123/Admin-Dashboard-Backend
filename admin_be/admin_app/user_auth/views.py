from rest_framework import generics
from admin_be.admin_app.user_auth.models.models import signup_model
from .serializers import Signup_serializer, Login_serializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class Signup_view(generics.CreateAPIView):
    queryset = signup_model.objects.all()
    serializer_class = Signup_serializer

class Login_view(generics.CreateAPIView):
    serializer_class = Login_serializer
    def post(self,request):
        username = request.data["username"]
        password = request.data["password"]

        user=authenticate(username=username,password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        else:
            return Response({"error":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)