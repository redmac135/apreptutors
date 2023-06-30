from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from auth_firebase.authentication import FirebaseAuthentication


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [FirebaseAuthentication]

    def get(self, request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data, many=True)
        response = {
            "status": status.HTTP_200_OK,
            "message": "success",
            "data": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
