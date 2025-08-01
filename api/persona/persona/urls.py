"""
URL configuration for persona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personapp import views

urlpatterns = [
    path('user/signup/', views.UserSignUpView.as_view(), name='signup'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/', views.AllUsersView.as_view(), name='users'),
    path('course/', views.AllCoursesView.as_view(), name='courses'),
    path('course/new/', views.CreateCourseView.as_view(), name='new_course'),
    path('course/<int:pk>', views.RUDCourseView.as_view(), name='rud_course')
]