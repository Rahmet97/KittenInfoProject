from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class UserRegisterSerializer(ModelSerializer):
    password1 = CharField(write_only=True)
    password2 = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password1']
        )

        return user
