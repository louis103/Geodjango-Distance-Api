from django.urls import path,include
from . import views

urlpatterns = [
    path("get-locations-within-distance/", views.getLocationsWithinDistance.as_view(),name="get-locations-within-distance")
]
