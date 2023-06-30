from rest_framework import serializers
from .models import Qualification, Timeslot, Location, CanTeachAt


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
    class Meta:
        model = CanTeachAt
        fields = [
            "instructor",
            "location",
        ]


class TimeslotSerializer(serializers.ModelSerializer):
    locations = CanTeachAtSerializer(many=True)

    class Meta:
        model = Timeslot
        fields = [
            "id",
            "instructor",
            "dayofweek",
            "time",
            "locations",
        ]


# WHERE YOU LEFT OFF: You need to figure out how to get a list of locations from a timeslot into the serializer, rn it's only 1 level deep but you need it 2 levels deep
