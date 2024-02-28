from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    password = serializers.CharField(write_only=True)  # Champ pour le mot de passe

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'age', 'password')  # Incluez le champ du mot de passe

    def create(self, validated_data):
        # Extrait le mot de passe du validated_data
        password = validated_data.pop('password', None)
        
        # Crée un nouvel utilisateur avec les données validées, sauf le mot de passe
        user = CustomUser.objects.create(**validated_data)
        
        # Définit le mot de passe pour le nouvel utilisateur s'il est fourni
        if password:
            user.set_password(password)
            user.save()
        
        return user


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print('///////////', user)
        token = super().get_token(user)

        # Ajoutez des champs personnalisés si nécessaire
        token['username'] = user.username
        # Ajoutez d'autres champs au besoin...

        return token