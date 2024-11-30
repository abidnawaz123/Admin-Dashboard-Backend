from rest_framework.serializers import ModelSerializer
from .models import User

class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
