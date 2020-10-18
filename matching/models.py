from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, Group as AbstractGroup, BaseUserManager, _user_has_perm)
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from geopy.distance import geodesic
from .utils.stl import canPrint

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



class Location(BaseModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  lat = models.FloatField(null=False, blank=False, default=0.0)
  lng = models.FloatField(null=False, blank=False, default=0.0)



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=150, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField('email address', blank=True)
    is_staff = models.BooleanField('is_staff', default=False)
    is_active = models.BooleanField('is_active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    lat = models.FloatField('lat', default=0)
    lng = models.FloatField('lng', default=0)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)

class ForeignedUserModel(BaseModel):
  user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=False, blank=False, default=0)
  class Meta:
    abstract = True

class Group(AbstractGroup):
  pass

class Printer3d(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  max_width = models.FloatField(null=False, blank=False, default=0.0) #mm
  max_height = models.FloatField(null=False, blank=False, default=0.0) #mm
  max_depth = models.FloatField(null=False, blank=False, default=0.0) #mm
  lat = models.FloatField(null=True, blank=True, default=0.0)
  lng = models.FloatField(null=True, blank=True, default=0.0)

  def printable(self, object3d):
    return canPrint([ self.max_width, self.max_height, self.max_depth ], object3d.stl.path)
  
  def distance(self, object3d):
    lat1 = self.lat
    lng1 = self.lng
    if self.lat is None or self.lng is None:
      lat1 = self.user.lat
      lng1 = self.user.lng
    
    lat2 = object3d.user.lat
    lng2 = object3d.user.lng

    meter = geodesic((lat1, lng1), (lat2, lng2)).m
    return meter
      

class Filament3d(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  genre = models.CharField(max_length=256, null=False, blank=False, default='')
  thin = models.FloatField(null=False, blank=False, default=0.5) # mm
  
class Object3d(ForeignedUserModel):
  name = models.CharField(max_length=256, null=False, blank=False, default='')
  stl = models.FileField(upload_to='uploads/', null=False, blank=False)
