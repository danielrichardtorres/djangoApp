from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
import uuid
from django import forms
import datetime

# Create your models here.


# Custom User Model (tied to settings via AUTH_USER_MODEL)
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        # extra_fields.__setattr__("first_name", extra_fields.get("first_name"))
        # extra_fields.setdefault("user_type", "student")

        # extra_fields.setdefault("user_type", "schedule_admin")
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("user_type", 1)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        # extra_fields.setdefault("user_type", "student")
        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError(_("Superuser must have is_staff=True."))
        # if extra_fields.get("is_superuser") is not True:
        #     raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Client(models.Model):
    id = models.UUIDField(
        _("client_id"), primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField("name", max_length=150, blank=True)

    signupdate = models.DateField("Sign Up Date", default=datetime.date.today())

    primaryEmail = models.EmailField(
        _("Primary email"), unique=True, max_length=254, blank=True
    )
    primaryPhone = models.CharField(_("Primary Phone"), max_length=50, blank=True)

    secondaryEmail = models.EmailField(_("Secondary email"), max_length=254, blank=True)
    secondaryPhone = models.CharField(_("Secondary Phone"), max_length=50, blank=True)

    studentEmail_1 = models.EmailField(_("Student 1 email"), max_length=254, blank=True)
    studentEmail_2 = models.EmailField(_("Student 2 email"), max_length=254, blank=True)

    address = models.CharField(_("Address"), max_length=200, blank=True, null=True)

    hours_available = models.IntegerField(_("hours available"), default=0)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    client_id = models.ForeignKey(
        Client, blank=True, null=True, on_delete=models.CASCADE
    )
    # schedule_admin/student/teacher
    class UserType(models.IntegerChoices):
        scheduleAdmin = 1, "Schedule Admin"
        student = 2, "Student"
        teacher = 3, "Teacher"
        parent = 4, "Parent"

    user_type = models.IntegerField(
        _("user type"), choices=UserType.choices, default=UserType.student
    )

    isStudent = property(lambda self: self.user_type == self.UserType.student)
    isTeacher = property(lambda self: self.user_type == self.UserType.teacher)
    isScheduleAdmin = property(
        lambda self: self.user_type == self.UserType.scheduleAdmin
    )
    isParent = property(lambda self: self.user_type == self.UserType.parent)

    first_name = models.CharField("first name", max_length=50)
    last_name = models.CharField("last_name", max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
