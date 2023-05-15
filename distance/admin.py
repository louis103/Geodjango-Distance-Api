from django.contrib import admin
from .models import Location

# Register your models here.
from django.contrib.gis import admin

admin.site.register(Location, admin.OSMGeoAdmin)
