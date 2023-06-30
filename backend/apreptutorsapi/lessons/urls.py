from django.urls import path
from .views import InstructorAPI

urlpatterns = [
    path("instructor/<int:pk>", InstructorAPI.as_view(), name="instructor-api")
]
