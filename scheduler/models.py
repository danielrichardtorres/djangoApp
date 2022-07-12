import datetime
from django.db import models
from users.models import CustomUser


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name="student",
        on_delete=models.CASCADE,
    )
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# Create your models here.
class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    notes = models.TextField()
    datetime = models.DateTimeField("datetime")
    duration = models.DurationField("duration")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.student} and {self.teacher} on {self.datetime.strftime('%Y-%m-%d %H:%M')}"


# class AppointmentTeacher(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
#     active = models.BooleanField()
#     order = models.IntegerField()

#     class Meta:
#         ordering = [
#             "order",
#         ]
