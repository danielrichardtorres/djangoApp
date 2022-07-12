from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Client

# Remove Group Model from admin. We're not using it.
from django.contrib.auth.models import Group

# from .forms import UserAdminCreationForm, UserAdminChangeForm Need to make these
# see https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model

admin.site.unregister(Group)


class CustomUserAdmin(admin.ModelAdmin):
    # exclude = ("username",)
    # model = CustomUser

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_display = ("email", "first_name", "last_name", "user_type")
    # list_filter = ("email", "is_staff", "is_active", "user_type")
    # fieldsets = (
    #     (
    #         None,
    #         {"fields": ("email", "password", "user_type", "first_name", "last_name")},
    #     ),
    #     (
    #         "Permissions",
    #         {"fields": ("is_staff", "is_active")},
    #     ),
    # )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("email", "password1", "password2"),
    #         },
    #     ),
    # )
    # search_fields = ("email", "user_type", "first_name", "last_name")
    pass
    # ordering = ("email",)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    # list_display = ("id", "parent1", "student1")
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Client, ClientAdmin)
