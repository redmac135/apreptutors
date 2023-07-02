from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from auth_firebase.authentication import FirebaseAuthentication

import json


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
        timeslots = self.model_class.objects.filter(
            instructor__instructorqualification_set__qualification__pk=qualification_pk
        )
        serializer = self.serializer_class(timeslots, many=True)
        return Response(serializer.data)


class InstructorSignupAPI(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        data = json.loads(request.body)
        print(data)
        user: Profile = self.authentication_classes[0].authenticate(
            FirebaseAuthentication(), request
        )[0]
        if user.is_teacher:
            raise PermissionError("You may only fill this out ONCE")
        user.set_teacher(True)

        # Create Instructor Qualifications
        for subject_pk in data["subjects"]:
            print("subject_pk: " + str(subject_pk))
            InstructorQualification.create_instructorqualification(
                instructor=user, qualification=Qualification.objects.get(pk=subject_pk)
            )

        # Create CanTeachAt Instances
        for location_pk in data["locations"]:
            print("location_pk: " + str(location_pk))
            CanTeachAt.create_relationship(
                instructor=user, location=Location.objects.get(pk=location_pk)
            )

        # Create Timeslot Instances
        for time in data["timeslots"]["sunday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.SUNDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["monday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.MONDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["tuesday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.TUESDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["wednesday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.WEDNESDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["thursday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.THURSDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["friday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.FRIDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["saturday"]:
            print("time: " + str(time))
            Timeslot.create_timeslot(
                weekday=Timeslot.SATURDAY, start_time=time, instructor=user
            )

        return Response(status=status.HTTP_200_OK)
