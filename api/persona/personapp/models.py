from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
class UserModel(AbstractUser):
    email = models.EmailField("", max_length=254, unique=True)
    role = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to="../avatars", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], default='avatars/default.jpg')
    
    def __str__(self):
        return f"<User {self.username}>"

class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.CharField(max_length=100, null=True) # ! Separated by comma
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    lessons = models.ManyToManyField('LessonModel', through='CourseLessons', related_name='lessons')

    def __str__(self):
        return f"<Course {self.name} by {self.user.username}>"


class LessonModel(models.Model):
    name = models.CharField(max_length=50)
    blocks = models.JSONField(default=dict) # ! Example in `course.example.json`

class CourseLessons(models.Model):
    lessons = models.ForeignKey(LessonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)