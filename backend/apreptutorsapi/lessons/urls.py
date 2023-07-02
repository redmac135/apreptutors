from django.urls import path
from .views import *

urlpatterns = [
    path("instructor/<int:pk>", InstructorAPI.as_view(), name="instructor-api"),
    path("locations/", LocationsListAPI.as_view(), name="locations-api"),
    path("timeslot/<int:pk>", TimeslotAPI.as_view(), name="timeslot-api"),
    path(
        "timeslots/<int:qualification_pk>",
        TimeslotsListAPI.as_view(),
        name="timeslots-api",
    ),
    path("qualifications/", QualificationsListAPI.as_view(), name="qualifications-api"),
    path("createtutor/", InstructorSignupAPI.as_view(), name="createtutor-api"),
    path("registeredlessons/", RegisteredLessonsAPI.as_view(), name="registeredlessons-api"),
]
