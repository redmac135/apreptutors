from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from auth_firebase.authentication import FirebaseAuthentication

import json
import hashlib


# Create your views here.
class InstructorAPI(APIView):
    model_class = Profile
    serializer_class = InstructorSerializer

    def get(self, request, pk):
        timeslot = self.model_class.objects.get(pk=pk)
        serializer = self.serializer_class(timeslot)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QualificationsListAPI(APIView):
    model_class = Qualification
    serializer_class = QualificationSerializer

    def get(self, request):
        qualifications = self.model_class.objects.all()
        serializer = self.serializer_class(qualifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LocationsListAPI(APIView):
    model_class = Location
    serializer_class = LocationSerializer

    def get(self, request):
        locations = self.model_class.objects.all()
        serializer = self.serializer_class(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserTypeAPI(APIView):
    model_class = Profile

    authentication_classes = [FirebaseAuthentication]

    def get(self, request):
        user = self.authentication_classes[0].authenticate(
            FirebaseAuthentication(), request
        )[0]
        response = {
            "is_student": user.is_student,
            "is_teacher": user.is_teacher,
        }
        return Response(response, status=status.HTTP_200_OK)


class TimeslotAPI(APIView):
    model_class = Timeslot
    serializer_class = TimeslotSerializer

    def get(self, request, pk):
        timeslot = self.model_class.objects.get(pk=pk)
        serializer = self.serializer_class(timeslot)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TimeslotsListBySubjectAPI(APIView):
    model_class = Timeslot
    serializer_class = TimeslotSerializer

    def get(self, request, qualification_pk):
        timeslots = self.model_class.objects.filter(
            instructor__instructorqualification_set__qualification__pk=qualification_pk,
            is_available=True,
        )
        serializer = self.serializer_class(timeslots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TimeslotsListAPI(APIView):
    model_class = Timeslot
    serializer_class = TimeslotSerializer

    def get(self, request):
        response = []
        subjects = Qualification.objects.all()
        for subject in subjects:
            valid_timeslots = self.model_class.objects.filter(
                instructor__instructorqualification_set__qualification=subject,
                is_available=True,
            )
            data = self.serializer_class(valid_timeslots, many=True).data
            location_ids = set()
            for timeslot in data:
                for location in timeslot["instructor"].pop("canteachat_set"):
                    location_ids.add(location["location"]["pk"])
                timeslot["locations"] = list(location_ids)
            response.append(
                {
                    "subjectId": subject.pk,
                    "timeslots": data,
                }
            )
        return Response(response, status=status.HTTP_200_OK)


class InstructorSignupAPI(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        data = json.loads(request.body)
        user: Profile = self.authentication_classes[0].authenticate(
            FirebaseAuthentication(), request
        )[0]

        # Ensure form only filled out once
        if user.is_teacher:
            raise PermissionError("You may only fill this out ONCE")

        # Check that Verification code works
        verification_code = data["verification"]
        correct_code = str(hashlib.md5(user.email.encode()).hexdigest())
        if not verification_code == correct_code:
            return Response(
                {"reponse": "Invalid verification code."}, status=status.HTTP_200_OK
            )

        user.set_teacher(True)
        user.save()

        # Create Instructor Qualifications
        for subject_pk in data["subjects"]:
            InstructorQualification.create_instructorqualification(
                instructor=user, qualification=Qualification.objects.get(pk=subject_pk)
            )

        # Create CanTeachAt Instances
        for location_pk in data["locations"]:
            CanTeachAt.create_relationship(
                instructor=user, location=Location.objects.get(pk=location_pk)
            )

        # Create Timeslot Instances
        for time in data["timeslots"]["sunday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.SUNDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["monday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.MONDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["tuesday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.TUESDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["wednesday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.WEDNESDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["thursday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.THURSDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["friday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.FRIDAY, start_time=time, instructor=user
            )

        for time in data["timeslots"]["saturday"]:
            Timeslot.create_timeslot(
                weekday=Timeslot.SATURDAY, start_time=time, instructor=user
            )

        return Response(
            {"response": "Instructor profile created."}, status=status.HTTP_200_OK
        )


class RegisteredLessonsAPI(APIView):
    model_class = Lesson
    serializer_class = LessonSerializer
    authentication_classes = [FirebaseAuthentication]

    # type: "student" | "teacher"
    def get(self, request, type: str):
        user: Profile = self.authentication_classes[0].authenticate(
            FirebaseAuthentication(), request
        )[0]

        if type == "student":
            lessons = self.model_class.objects.filter(student__uid=user.uid)
        elif type == "teacher":
            lessons = self.model_class.objects.filter(
                timeslot__instructor__uid=user.uid
            )
        else:
            raise TypeError("type may only be 'student' or 'teacher'.")

        serializer = self.serializer_class(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateLessonAPI(APIView):
    model_class = Lesson
    authentication_classes = [FirebaseAuthentication]
    ALLOWED_LESSONS_PER_WEEK = [1, 2]

    def post(self, request):
        data = json.loads(request.body)
        user: Profile = self.authentication_classes[0].authenticate(
            FirebaseAuthentication(), request
        )[0]

        lesson_amount = 0
        for value in data["timeslots"].values():
            lesson_amount += len(value)

        if not lesson_amount in self.ALLOWED_LESSONS_PER_WEEK:
            raise ValueError("Wrong number of lessons")
        location = Location.objects.get(pk=data["location"])
        subject = Qualification.objects.get(pk=data["subject"])
        timeslot_criteria = []
        for weekday_long, time_pk_list in data["timeslots"].items():
            for time_pk in time_pk_list:
                timeslot_criteria.append(
                    (weekday_long[0:3].upper(), Timeslot.ALLOWED_TIMES[time_pk][0])
                )
        timeslots = Timeslot.find_timeslots(timeslot_criteria, subject, location)
        for timeslot in timeslots:
            self.model_class.create_lesson(
                timeslot=timeslot,
                student=user,
                location=location,
                subject=subject,
                num_students=int(data["num_students"]),
            )

        return Response(status=status.HTTP_200_OK)
