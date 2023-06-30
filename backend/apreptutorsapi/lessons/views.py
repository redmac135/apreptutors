from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class InstructorAPI(APIView):
    model_class = Profile
    serializer_class = InstructorSerializer

    def get(self, request, pk):
        timeslot = self.model_class.objects.get(pk=pk)
        serializer = self.serializer_class(timeslot)
        return Response(serializer.data)

class LocationsListAPI(APIView):
    model_class = Location
    serializer_class = LocationSerializer

    def get(self, request):
        locations = self.model_class.objects.all()
        serializer = self.serializer_class(locations, many=True)
        return Response(serializer.data)