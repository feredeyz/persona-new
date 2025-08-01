from personapp import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .models import UserModel, CourseModel
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
import logging
from datetime import timedelta
from personapp.permissions import IsAuthor

logger = logging.getLogger(__name__)





#! --------------
#!  Users stuff
#! --------------
class UserSignUpView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserSignupSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(f"Создан пользователь {serializer.validated_data}")
        return Response(
            {"message": "Пользователь успешно создан"},
            status=HTTP_201_CREATED,
            headers=headers
        )

class UserLoginView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            response = Response({"message": "Успешный вход в аккаунт"}, status=HTTP_200_OK)
            response.set_cookie(
                "access_token", token, max_age=timedelta(days=30), # TODO: change secure
                secure=False, httponly=True, samesite='Strict'
            )
            headers = self.get_success_headers(serializer.data)
            response.headers = headers
            logger.info(f"Пользователь {"впервые" if created else ""} вошёл в аккаунт {user.username}") # тут был марк товбин
            return response
        else:
            return Response(serializer.error_messages, status=HTTP_400_BAD_REQUEST)

class AllUsersView(generics.ListAPIView):
    serializer_class = serializers.UserListSerializer
    queryset = UserModel.objects.all()

#! --------------
#! Courses stuff
#! --------------

class AllCoursesView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    queryset = CourseModel.objects.all()

class CreateCourseView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CourseSerializer
    queryset = CourseModel.objects.all()

class RUDCourseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthor]