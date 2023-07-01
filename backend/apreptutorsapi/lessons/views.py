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

class QualificationsListAPI(APIView):
    model_class = Qualification
    serializer_class = QualificationSerializer

    def get(self, request):
        qualifications = self.model_class.objects.all()
        serializer = self.serializer_class(qualifications, many=True)
        return Response(serializer.data)

class LocationsListAPI(APIView):
    model_class = Location
    serializer_class = LocationSerializer

    def get(self, request):
        locations = self.model_class.objects.all()
        serializer = self.serializer_class(locations, many=True)
        return Response(serializer.data)
    

# class UserTypeAPI(APIView):
#     model_class = Profile

#     def get(self, request, pk):
#         user = self.model_class.objects.get(pk=pk)
#         response = {
#             "type": 
#         }
    

class TimeslotAPI(APIView):
    model_class = Timeslot
    serializer_class = TimeslotSerializer

    def get(self, request, pk):
        timeslot = self.model_class.objects.get(pk=pk)
        serializer = self.serializer_class(timeslot)
        return Response(serializer.data)

class TimeslotsListAPI(APIView):
    model_class = Timeslot
    serializer_class = TimeslotSerializer

    def get(self, request, qualification_pk):
        timeslots = self.model_class.objects.filter(instructor__instructorqualification_set__qualification__pk=qualification_pk)
        serializer = self.serializer_class(timeslots, many=True)
        return Response(serializer.data)