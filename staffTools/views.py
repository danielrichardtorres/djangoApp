from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_schedule(request):
    context = {"title": "staff create schedule"}
    return render(request, "staffTools/create_schedule.html", context=context)


@login_required
def home(request):
    context = {"title": "staff home"}
    return render(request, "staffTools/home.html", context=context)
