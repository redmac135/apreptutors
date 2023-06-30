from rest_framework import serializers
from .models import Qualification, Timeslot, Location, CanTeachAt, Profile


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = [
            "id",
            "type",
            "name",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "name",
            "address",
        ]


class CanTeachAtSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = CanTeachAt
        fields = [
            "instructor",
            "location",
        ]


# TODO: Check that profile object passed is_teacher
class InstructorSerializer(serializers.ModelSerializer):
    canteachat_set = CanTeachAtSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            "display_name",
            "email",
            "canteachat_set",
        ]


# WHERE YOU LEFT OFF: You need to figure out how to get a list of locations from a timeslot into the serializer, rn it's only 1 level deep but you need it 2 levels deep
