from .serializers import UserSignupSerializer,  UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .models import UserModel
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class UserSignUpView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Пользователь успешно создан"},
            status=HTTP_201_CREATED,
            headers=headers
        )

class UserLoginView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            logger.info(f"Пользователь {"впервые" if created else ""} вошёл в аккаунт {user.username}")
            return Response({"token": token.key}, status=HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=HTTP_400_BAD_REQUEST)
