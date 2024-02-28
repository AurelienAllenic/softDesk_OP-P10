from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    # Ajoutez d'autres champs ici en fonction de vos besoins

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'age')  # Incluez tous les champs de votre modèle

    def validate(self, attrs):
        # Validez les champs uniquement lors de la mise à jour (PUT ou PATCH)
        if self.instance is not None:
            for field in attrs.keys():
                if field not in self.Meta.fields:
                    raise serializers.ValidationError({field: "This field cannot be updated."})
        return attrs

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajoutez des champs personnalisés si nécessaire
        token['username'] = user.username
        # Ajoutez d'autres champs au besoin...

        return token