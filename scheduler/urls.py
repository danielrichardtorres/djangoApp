from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="scheduler-home"),
    path("about/", views.about, name="scheduler-about"),
    path("add_client/", views.addClient, name="scheduler-addclient"),
    path("myschedule/", views.studentScheduleView, name="scheduler-myschedule"),
]
