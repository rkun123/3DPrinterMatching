from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, GroupSerializer, Printer3dSerializer, LocationSerializer, Filament3dSerializer, Object3dSerializer
from .models import Printer3d, Location, Filament3d, Object3d

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

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class LocationViewSet(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class Filament3dViewSet(viewsets.ModelViewSet):
  queryset = Filament3d.objects.all()
  serializer_class = Filament3dSerializer
  permission_classes = [permissions.IsAuthenticated]

class Object3dViewSet(viewsets.ModelViewSet):
  queryset = Object3d.objects.all()
  serializer_class = Object3dSerializer
  permission_classes = [permissions.IsAuthenticated]