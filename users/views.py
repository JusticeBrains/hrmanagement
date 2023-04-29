from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import CustomUserSerializer

User = get_user_model()

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    filterset_fields = "__all__"
