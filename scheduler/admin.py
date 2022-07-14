from django.contrib import admin
from .models import Subject, Student, Teacher, AppointmentInstance, RepeatingAppointment

# Register your models here.
# class AppointmentAdmin(admin.ModelAdmin):
#     model = Appointment
#     list_display = (
#         "datetime",
#         "duration",
#         "teacher",
#         "student",
#     )


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(AppointmentInstance)
admin.site.register(RepeatingAppointment)
