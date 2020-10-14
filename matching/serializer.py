from django.contrib.auth.models import User, Group
from .models import Printer3d
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'groups', 'last_login']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class Printer3dSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Printer3d
    fields = ['name', 'max_width', 'max_height', 'max_depth']