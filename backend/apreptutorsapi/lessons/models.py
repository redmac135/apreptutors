from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user)


class Qualification(models.Model):
    IB_COURSE_TYPES = [("HL", "HL"), ("SL", "SL")]

    type = models.CharField(max_length=2, choices=IB_COURSE_TYPES)
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.type + " " + self.name


class InstructorQualification(models.Model):
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.instructor) + " " + str(self.qualification)


class Timeslot(models.Model):
    SUNDAY = "SUN"
    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"
    SATURDAY = "SAT"
    DAYS_OF_WEEK = [
        (SUNDAY, "Sunday"),
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
    ]

    is_available = models.BooleanField()
    weekday = models.CharField(max_length=3)
    time = models.TimeField()
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.time) + " " + self.weekday + " " + str(self.instructor)


class Lesson(models.Model):
    timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Qualification, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return str(self.subject) + " " + str(self.timeslot) + " " + str(self.student)
