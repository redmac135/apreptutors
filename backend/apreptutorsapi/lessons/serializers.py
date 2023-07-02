from rest_framework import serializers
from .models import Qualification, Timeslot, Location, CanTeachAt, Profile


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


class TimeslotSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()

    class Meta:
        model = Timeslot
        fields = [
            "weekday",
            "start_time",
            "instructor",
        ]
