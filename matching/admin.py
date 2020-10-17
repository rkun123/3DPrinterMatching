from django.contrib import admin
from matching.models import Printer3d, Location, Filament3d, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Location)
admin.site.register(Printer3d)
admin.site.register(Filament3d)

class CustomUserAdmin(UserAdmin):
    ...
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('lat','lng')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('lat','lng')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)