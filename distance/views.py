from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from rest_framework.views import APIView

from .serializers import LocationSerializer
from .models import Location

from rest_framework.response import Response
# Create your views here.

class getLocationsWithinDistance(APIView):
    
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                print(serializer.data)
                
                data = serializer.data
                
                print(data)
                
                pnt = GEOSGeometry('POINT({} {})'.format(data['long'], data['lat']), srid=4326)
                
                locations = Location.objects.all()
                
                qs = Location.objects.all().filter(point__distance_lt=(pnt, D(km=1000)))
                
                print(len(qs))
                
                return Response({'DATA', str(qs)})
                
            except Exception as e:
                print(e)  
                
        return Response(serializer.errors)

