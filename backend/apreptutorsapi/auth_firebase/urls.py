from django.urls import path
from . import views

urlspatterns = [
    path("api/students/", views.ProfileAPIView.as_view(), name="api-profiles"),
]
