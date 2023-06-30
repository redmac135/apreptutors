from typing import Any
from django.db import models
from firebase_admin import auth


class ProfileManager(models.Manager):
    def create_teacher(self, uid, **kwargs: Any):
        user = auth.get_user(uid)
        display_name = user.getDisplayName()
        email = user.getEmail()

        return super(self, ProfileManager).create(
            uid=uid,
            display_name=display_name,
            email=email,
            is_student=False,
            is_teacher=True,
        )

    def create_student(self, uid, **kwargs: Any):
        user = auth.get_user(uid)
        display_name = user.getDisplayName()
        email = user.getEmail()

        return super(self, ProfileManager).create(
            uid=uid,
            display_name=display_name,
            email=email,
            is_student=True,
            is_teacher=False,
        )

    def get_or_create_student(self, uid, **kwargs: Any):
        if not self.filter(uid=uid).exists():
            return self.create_student(uid, **kwargs)
        return self.get(uid=uid)
