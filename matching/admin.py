from django.contrib import admin
from matching.models import Printer3d, Location, Filament3d

# Register your models here.

admin.site.register(Location)
admin.site.register(Printer3d)
admin.site.register(Filament3d)
