import datetime
from django.db import models
from users.models import CustomUser


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, default="")
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name="student",
        on_delete=models.CASCADE,
    )
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    id = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# create a model for repeating appointments with a student and a subject
class RepeatingAppointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time(8, 0, 0))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    frequency = models.CharField(max_length=10, default="weekly")

    def __str__(self):
        return f"{self.student.user.first_name} {self.subject.name} {self.date} {self.time}"


# class for the appointment instances on specifc days and times
class AppointmentInstance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.first_name} {self.subject.name} {self.date} {self.time}"
