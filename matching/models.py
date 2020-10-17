from django.db import models
from django.contrib.auth.models import (User, UserManager as AbstractUserManager, Group as AbstractGroup, _user_has_perm)
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class BaseModel(models.Model):
  createdAt = models.DateTimeField(null=False, blank=False, auto_now_add=True)
  updatedAt = models.DateTimeField(null=False, blank=False, auto_now=True)
  deletedAt = models.DateTimeField(null=True, blank=True)

  class Meta:
    abstract = True
  
  def delete(self):
    self.deletedAt = timezone.now()
    self.save()


class UserManager(AbstractUserManager):
  pass

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)

class ForeignedUserModel(BaseModel):
  user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, default=0)
  class Meta:
    abstract = True

class Group(AbstractGroup):
  pass

class Location(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  lat = models.FloatField(null=False, blank=False, default=0.0)
  lng = models.FloatField(null=False, blank=False, default=0.0)

class Printer3d(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  max_width = models.FloatField(null=False, blank=False, default=0.0) #mm
  max_height = models.FloatField(null=False, blank=False, default=0.0) #mm
  max_depth = models.FloatField(null=False, blank=False, default=0.0) #mm

class Filament3d(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  genre = models.CharField(max_length=256, null=False, blank=False, default='')
  thin = models.FloatField(null=False, blank=False, default=0.5) # mm
  
class Object3d(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  stl = models.FileField(upload_to='uploads/', null=False, blank=False)
