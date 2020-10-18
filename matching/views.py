from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login
from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import UserSerializer, GroupSerializer, Printer3dSerializer, LocationSerializer, Filament3dSerializer, Object3dSerializer, PrintablesSerializer, RequestSerializer, DMSerializer
from .models import Printer3d, Location, Filament3d, Object3d, CustomUser, Request, DM

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all().order_by('-date_joined')
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

  @action(detail=True, permission_classes=[permissions.IsAuthenticated])
  def printables(self, request, pk=None):
    obj = Object3d.objects.get(pk=pk)
    printers = Printer3d.objects.all()
    printable_printers = []

    for printer in printers.iterator():
      if printer.printable(obj):
        printer_dict = {}
        printer_dict['name'] = printer.name
        printer_dict['max_width'] = printer.max_width
        printer_dict['max_height'] = printer.max_height
        printer_dict['max_depth'] = printer.max_depth
        printer_dict['lat'] = printer.lat
        printer_dict['lng'] = printer.lng
        printer_dict['distance'] = printer.distance(obj)
        printable_printers.append(printer_dict)

    sorted_printers = sorted(printable_printers, key= lambda printer: printer['distance'])
    serialize = PrintablesSerializer(data=sorted_printers, many=True)

    if serialize.is_valid():
      return Response(serialize.data)
    else:
      return JsonResponse({
        "error": serialize.errors
      })

class RequestViewSet(viewsets.ModelViewSet):
  queryset = Request.objects.all()
  serializer_class = RequestSerializer
  permission_classes = [permissions.IsAuthenticated]

class DMViewSet(viewsets.ModelViewSet):
  queryset = DM.objects.all()
  serializer_class = DMSerializer
  permission_classes = [permissions.IsAuthenticated]