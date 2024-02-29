from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    password = serializers.CharField(write_only=True)
    consent = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'age', 'password', 'consent')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        
        user = CustomUser.objects.create(**validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print('///////////', user)
        token = super().get_token(user)

        token['username'] = user.username

        return token