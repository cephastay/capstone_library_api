from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, generics, permissions

from accounts.serializers import UserSerializer, ProfileInfoSerializer
from accounts.permissions import IsUserOrReadOnly

# Create your views here.
class Register(generics.CreateAPIView):
    """
    For Creating, and Listing Users in the Library Management API 
    """
    queryset = get_user_model().objects.all()

    serializer_class = UserSerializer

class UserView(generics.RetrieveUpdateDestroyAPIView):
    """This is for retrieving updating or Destroy user instances"""

    permission_classes = [IsUserOrReadOnly]
    serializer_class = ProfileInfoSerializer
    queryset = get_user_model().objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)