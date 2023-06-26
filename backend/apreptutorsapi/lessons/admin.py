from django.contrib import admin
from models import Profile, Qualification, InstructorQualification, Timeslot, Lesson

# Register your models here.
admin.site.register(Profile)
admin.site.register(Qualification)
admin.site.register(InstructorQualification)
admin.site.register(Timeslot)
admin.site.register(Lesson)
