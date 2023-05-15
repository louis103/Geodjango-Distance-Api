from django.db import models
from django.contrib.gis.db import models as giomodels

# Create your models here.
class Location(models.Model):
    point = giomodels.PointField(srid=4326, blank=True, null=True)
    
    # def __str__(self):
    #     return self.point
    