from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, GroupSerializer, Printer3dSerializer
from .models import Printer3d

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]

class Printer3dViewSet(viewsets.ModelViewSet):
  queryset = Printer3d.objects.all()
  serializer_class = Printer3dSerializer
  permission_classes = [permissions.IsAuthenticated]