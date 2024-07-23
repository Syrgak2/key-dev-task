from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
