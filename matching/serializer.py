from django.contrib.auth.models import Group
from .models import Printer3d, Location, Filament3d, Object3d, CustomUser, Request, DM
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.serializers import FloatField

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'email', 'groups', 'last_login', 'lat', 'lng']

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class Printer3dSerializer(serializers.ModelSerializer):
  class Meta:
    model = Printer3d
    fields = ['id', 'name', 'max_width', 'max_height', 'max_depth', 'lat', 'lng', 'user']
    depth = 1

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['id', 'name', 'lat', 'lng', 'user']
    depth = 1

class Filament3dSerializer(serializers.ModelSerializer):
  class Meta:
    model = Filament3d
    fields = ['id', 'name', 'genre', 'thin', 'user']

class Object3dSerializer(serializers.ModelSerializer):
  class Meta:
    model = Object3d
    fields = ['id', 'name', 'stl', 'user']

class PrintablesSerializer(serializers.ModelSerializer):
  distance = FloatField()
  class Meta:
    model = Printer3d
    fields = ['id', 'name', 'max_width', 'max_height', 'max_depth', 'lat', 'lng', 'distance', 'user']
    depth = 1

class RequestSerializer(serializers.ModelSerializer):
  object_owner = serializers.PrimaryKeyRelatedField(read_only=True)
  printer_owner = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
    model = Request
    fields = ['id', 'object3d', 'printer3d', 'object_owner', 'printer_owner']
  
  def create(self, validated_data):
    object3d = validated_data['object3d']
    printer3d = validated_data['printer3d']
    return Request.objects.create(object_owner=object3d.user, printer_owner=printer3d.user, object3d=object3d, printer3d=printer3d)

  def update(self, instance, validated_data):
      instance.object3d = validated_data.get('object3d', instance.email)
      instance.printer3d = validated_data.get('printer3d', instance.content)
      instance.object_owner = instance.object3d.user
      instance.printer_owner = instance.printer3d.user
      return instance


class DMSerializer(serializers.ModelSerializer):
  class Meta:
    model = DM
    fields = ['id', 'sender', 'receiver', 'text']