from django.db import models
from .managers import ProfileManager


# Create your models here.
class Profile(models.Model):
    uid = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = ProfileManager()

    def __str__(self):
        return str(self.display_name)

    def set_teacher(self, is_teacher: bool):
        self.is_teacher = is_teacher
        return self
