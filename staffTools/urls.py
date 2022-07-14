from django.urls import path
from scheduler import views as scheduler_views
from . import views as staffTools_views

urlpatterns = [
    path("createschedule/", staffTools_views.create_schedule, name="build_schedule"),
]
