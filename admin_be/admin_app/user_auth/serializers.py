from admin_be.admin_app.user_auth.models.models import signup_model
from rest_framework import serializers



class Signup_serializer(serializers.ModelSerializer):
    class Meta:
        model = signup_model
        fields = '__all__'

class Login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()