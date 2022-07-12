from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *

# from django.contrib.auth.models import User
from django.conf import settings

from users.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # form is going  to create a new user
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "user_type",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class addClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
