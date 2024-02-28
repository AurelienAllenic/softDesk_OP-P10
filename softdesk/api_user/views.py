from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomTokenSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'email' in request.data and instance.email != request.data['email']:
            # L'email a changé, nous devons vérifier s'il est unique
            try:
                self.queryset.get(email=request.data['email'])
                return Response({"email": ["User with this email address already exists."]}, status=status.HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist:
                pass
        return super().put(request, *args, **kwargs)


class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer