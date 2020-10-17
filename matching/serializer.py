from django.contrib.auth.models import User, Group
from .models import Printer3d, Location, Filament3d
from rest_framework import serializers
from rest_framework.decorators import action

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'groups', 'last_login']

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class Printer3dSerializer(serializers.ModelSerializer):
  class Meta:
    model = Printer3d
    fields = ['name', 'max_width', 'max_height', 'max_depth', 'user']

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['name', 'lat', 'lng']
    depth = 1

  def destroy(self, request, pk=None):
    location = Location.objects.filter(pk=pk)
    location.delete()

class Filament3dSerializer(serializers.ModelSerializer):
  class Meta:
    model = Filament3d
    fields = ['name', 'genre', 'thin', 'user']
