from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField

class UserModel(AbstractUser):
    email = models.EmailField("", max_length=254, unique=True)
    role = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to="../avatars", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], default='avatars/default.jpg')
    
    def __str__(self):
        return f"<User {self.username}>"

class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tags = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        null=True,
        size=10,
        default=list
    )
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"<Course {self.name} by {self.user.username}>"

class LessonModel(models.Model):
    title = models.CharField(max_length=50)
    blocks = models. JSONField(default=list)
    course = models.ForeignKey(
        CourseModel,
        related_name='lessons',
        on_delete=models.CASCADE
    )