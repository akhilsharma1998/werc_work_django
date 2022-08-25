from django.contrib import admin
from django.urls import path, include
from enroll.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('userdetail/', UserDetail.as_view(), name='userdetail'),
    path('UpdateProfile/', UpdateProfile.as_view(), name='UpdateProfile'),
]