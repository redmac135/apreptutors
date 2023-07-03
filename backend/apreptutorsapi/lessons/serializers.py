from rest_framework import serializers
from .models import Qualification, Timeslot, Location, CanTeachAt, Profile, Lesson


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = [
            "pk",
            "type",
            "name",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "pk",
            "name",
            "address",
        ]


class CanTeachAtSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = CanTeachAt
        fields = [
            "pk",
            "instructor",
            "location",
        ]


# TODO: Check that profile object passed is_teacher
class InstructorSerializer(serializers.ModelSerializer):
    canteachat_set = CanTeachAtSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            "pk",
            "display_name",
            "email",
            "canteachat_set",
        ]


class LocationIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["pk"]


class SimpleCanTeachAtSerializer(serializers.ModelSerializer):
    location = LocationIdSerializer()

    class Meta:
        model = CanTeachAt
        fields = [
            "pk",
            "location",
        ]


class SimpleInstructorSerializer(serializers.ModelSerializer):
    canteachat_set = SimpleCanTeachAtSerializer()

    class Meta:
        model = Profile
        fields = [
            "pk",
            "canteachat_set",
        ]


class TimeslotSerializer(serializers.ModelSerializer):
    instructor = SimpleInstructorSerializer()

    class Meta:
        model = Timeslot
        fields = [
            "pk",
            "weekday",
            "start_time",
            "instructor",
        ]


class LessonSerializer(serializers.ModelSerializer):
    timeslot = TimeslotSerializer()
    subject = QualificationSerializer()

    class Meta:
        model = Lesson
        fields = [
            "timeslot",
            "subject",
        ]
