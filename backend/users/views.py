from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import viewsets

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer