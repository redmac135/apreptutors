from django.urls import path
from .views import *

urlpatterns = [
    path("instructor/<int:pk>", InstructorAPI.as_view(), name="instructor-api"),
    path("locations/", LocationsListAPI.as_view(), name="locations-api"),
    path("timeslot/<int:pk>", TimeslotAPI.as_view(), name="timeslot-api"),
    path("timeslots/all", TimeslotsListAPI.as_view(), name="timeslots-api"),
    path(
        "timeslots/<int:qualification_pk>",
        TimeslotsListBySubjectAPI.as_view(),
        name="timeslotsbysubject-api",
    ),
    path("qualifications/", QualificationsListAPI.as_view(), name="qualifications-api"),
    path("createtutor/", InstructorSignupAPI.as_view(), name="createtutor-api"),
    path("usertype/", UserTypeAPI.as_view(), name="usertype-api"),
    path(
        "registeredlessons/",
        RegisteredLessonsAPI.as_view(),
        name="registeredlessons-api",
    ),
]
