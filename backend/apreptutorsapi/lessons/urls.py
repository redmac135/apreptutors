from django.urls import path
from .views import *

urlpatterns = [
    path("instructor/<int:pk>", InstructorAPI.as_view(), name="instructor-api"),
    path("locations/", LocationsListAPI.as_view(), name="locations-api")
]
