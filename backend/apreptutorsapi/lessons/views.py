from django.shortcuts import render
from rest_framework.views import APIView
from .models import Timeslot
from .serializers import TimeslotSerializer
from rest_framework.response import Response


# Create your views here.
class TimeslotAPI(APIView):
    model_class = Timeslot
    serializer_class = TimeslotSerializer

    def get(self, request, pk):
        timeslot = self.model_class.objects.get(pk=pk)
        serializer = self.serializer_class(timeslot)
        return Response(serializer.data)
