from rest_framework import serializers
from .models import UserModel, CourseModel, LessonModel



#! --------------
#!  Users stuff
#! --------------
class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50, write_only=True)
    
    def validate(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = UserModel.objects.filter(username=username).first()
        if not user:
            raise serializers.ValidationError("Пользователь с данным именем пользователя уже существует.")
        if user.check_password(password):
            return user
        else:
            raise serializers.ValidationError("Неправильный пароль")


#! --------------
#! Courses stuff
#! --------------
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = ['title', 'blocks']

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, required=False)

    class Meta:
        model = CourseModel
        fields = ['id', 'name', 'description', 'tags', 'created_at', 'user', 'lessons']
        extra_kwargs = {
            'id': {"read_only": True},
            'user': {'read_only': True},
            'created_at': {'read_only': True}
        }
    
    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        course = CourseModel.objects.create(
            **validated_data,
            user=self.context['request'].user
        )
        for lesson_data in lessons_data:
            LessonModel.objects.create(course=course, **lesson_data)
        return course
