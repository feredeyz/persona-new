from rest_framework import serializers
from .models import UserModel, CourseModel

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