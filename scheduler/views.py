from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime

from users.forms import addClientForm
from .models import Subject, Student, Teacher, AppointmentInstance, RepeatingAppointment


# Create your views here
@login_required
def home(request):
    context = {"title": "Home"}

    if request.user.isStudent:

        return render(request, "scheduler/home.html", context=context)
    elif request.user.isTeacher:

        return render(request, "scheduler/home.html", context=context)
    elif request.user.isScheduleAdmin:

        return render(request, "staffTools/home.html", context=context)
    elif request.user.isParent:

        return render(request, "scheduler/home.html", context=context)
    else:
        return render(request, "scheduler/home.html", context=context)


@login_required
def studentScheduleView(request):
    relatedStudent = request.user.student.get()

    if isinstance(relatedStudent, Student):
        appointments = AppointmentInstance.objects.filter(student=relatedStudent)
    else:
        appointments = AppointmentInstance.objects.all()
    # print(appointments)

    dt = datetime.date.today()
    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=5)

    appointments = appointments.filter(datetime__range=[start, end])
    context = {"appointments": appointments}
    return render(request, "scheduler/appointment_list.html", context=context)


# @login_required
# def mySchedule(request):
#     appts = Appointment.objects.all()

#     dt = datetime.date.today()
#     start = dt - datetime.timedelta(days=dt.weekday())
#     end = start + datetime.timedelta(days=5)

#     # def daterange(start_date, end_date):
#     #     for n in range(int((end_date - start_date).days)):
#     #         yield start_date + datetime.timedelta(n)

#     # for single_date in daterange(start, end):
#     #     for appt in appointmentList:
#     #         # print(single_date)
#     #         # print(appt.datetime.date())
#     #         if appt.datetime.date() == single_date:
#     #             dayName = calendar.day_name[appt.datetime.weekday()]
#     #             # print(dayName, single_date)
#     #             # print(appt.datetime.time())
#     #             appointments[dayName].append(appt.datetime.time())

#     # for all the appointments for the given student logged in
#     # put them all in the appointments list
#     # give that to context and print them out
#     context = {
#         "appointments": appts,
#         "appointmentList": appts,
#         "title": "My Schedule",
#     }
#     # return render(request, "scheduler/home.html", context=context)
#     return render(request, "scheduler/myschedule.html", context=context)


def about(request):
    return render(request, "scheduler/about.html", {"title": "About"})


def addClient(request):
    ##this should really be in the users app
    # too tired to move it rn

    if request.method == "POST":
        form = addClientForm(request.POST)
        if form.is_valid():
            form.save()
            client = form.cleaned_data.get("name")
            messages.success(request, f"Account created for {client}!")
            return redirect("scheduler-home")
    else:
        form = addClientForm()
    return render(
        request,
        "scheduler/addClient.html",
        context={"form": form, "title": "Add Client"},
    )
