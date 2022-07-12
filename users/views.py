from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from flask import flash
from .forms import UserRegistrationForm

# Create your views here.

# registration page
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("email")
            messages.success(
                request, f"Account created for {user}! Please go ahead and log in."
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", context={"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
