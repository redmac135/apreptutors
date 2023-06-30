from django.urls import path
from . import views

urlpatterns = [
    path("profiles/", views.ProfileAPIView.as_view(), name="api-profiles"),
]
