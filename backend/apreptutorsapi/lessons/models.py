import datetime
from django.db import models
from auth_firebase.models import Profile


# Create your models here.
class Qualification(models.Model):
    IB_COURSE_TYPES = [("HL", "HL"), ("SL", "SL")]

    type = models.CharField(max_length=2, choices=IB_COURSE_TYPES)
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.type + " " + self.name

    def check_qualified(self, instructor: Profile):
        if not instructor.is_teacher:
            raise PermissionError("Not Teacher")
        return (
            InstructorQualification.get_qualifications_queryset(instructor)
            .filter(qualification=self)
            .exists()
        )


class InstructorQualification(models.Model):
    instructor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="instructorqualification_set"
    )
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.instructor) + " " + str(self.qualification)

    @classmethod
    def create_instructorqualification(
        cls, instructor: Profile, qualification: Qualification
    ):
        if not instructor.is_teacher:
            raise PermissionError("Not Teacher")
        obj, created = cls.objects.get_or_create(
            instructor=instructor, qualification=qualification
        )
        return obj

    @classmethod
    def get_qualifications_queryset(cls, instructor: Profile):
        if not instructor.is_teacher:
            raise PermissionError("Not Teacher")
        return cls.objects.filter(instructor=instructor)


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
    ALLOWED_TIMES = [
        (datetime.time(9, 0, 0), "9:00"),
        (datetime.time(10, 30, 0), "10:30"),
        (datetime.time(12, 0, 0), "12:00"),
        (datetime.time(13, 30, 0), "13:30"),
        (datetime.time(14, 0, 0), "14:00"),
        (datetime.time(16, 30, 0), "16:30"),
        (datetime.time(18, 0, 0), "18:00"),
        (datetime.time(19, 30, 0), "19:30"),
        (datetime.time(21, 0, 0), "21:00"),
    ]

    is_available = models.BooleanField()
    weekday = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(choices=ALLOWED_TIMES)
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.start_time) + " " + self.weekday + " " + str(self.instructor)

    @classmethod
    def create_timeslot(
        cls,
        weekday: str,
        start_time: int,
        instructor: Profile,
        is_available: bool = True,
    ) -> None:
        if not instructor.is_teacher:
            raise PermissionError("Not Teacher")
        else:
            obj, created = cls.objects.get_or_create(
                weekday=weekday,
                start_time=cls.ALLOWED_TIMES[start_time][0],
                instructor=instructor,
                is_available=is_available,
            )
            return obj

    # Pass in a list of criteria and this method will return a list of timeslots which fits the criteria
    @classmethod
    def find_timeslots(cls, timeslot_criteria, subject, location):
        possible_instructors = []
        possible_timeslots = []
        for weekday, start_time in timeslot_criteria:
            timeslots = cls.objects.filter(
                weekday=weekday,
                start_time=start_time,
                instructor__instructorqualification_set__qualification=subject,
                instructor__canteachat_set__location=location,
            )
            instructors = [timeslot.instructor for timeslot in timeslots]
            possible_timeslots.append(timeslots)
            possible_instructors.append(instructors)
        
        reduced_instructors = set(possible_instructors[0])
        for s in possible_instructors[1:]:
            reduced_instructors.intersection_update(s)
        
        if not reduced_instructors:
            raise LookupError("No Valid Timeslots")
    
        # Pick first instructor
        instructor = next(iter(reduced_instructors))
        final_list = []
        for timeslots in possible_timeslots:
            valid_timeslots = [timeslot for timeslot in timeslots if timeslot.instructor == instructor]
            final_list.append(valid_timeslots[0])
        
        return final_list
            

    def set_unavailable(self):
        self.is_available = False
        self.save()
        return self


class Location(models.Model):
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name


class CanTeachAt(models.Model):
    instructor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="canteachat_set"
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.instructor) + " at " + str(self.location)

    @classmethod
    def create_relationship(cls, instructor: Profile, location: Location):
        if not instructor.is_teacher:
            raise PermissionError("Not Teacher")
        obj, created = cls.objects.get_or_create(
            instructor=instructor, location=location
        )
        return obj


class Lesson(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Qualification, null=True, on_delete=models.SET_NULL)
    num_students = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.subject) + " " + str(self.timeslot) + " " + str(self.student)

    @classmethod
    def create_lesson(
        cls, timeslot: Timeslot, student: Profile, subject: Qualification, location: Location, num_students: int
    ):
        if not student.is_student:
            raise PermissionError("Not Student")
        instructor = timeslot.instructor
        if not subject.check_qualified(instructor):
            raise PermissionError("Not Qualified")
        obj = cls.objects.get_or_create(
            timeslot=timeslot, student=student, subject=subject, location=location, num_students=num_students
        )
        timeslot.set_unavailable()
        return obj
