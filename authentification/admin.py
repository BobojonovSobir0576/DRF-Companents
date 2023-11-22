""" Django Libraries """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentification.models import CustomUser
from authentification.forms import ChangeUser, CreasteUser


class NewMyUser(UserAdmin):
    """New User"""

    add_form = CreasteUser
    form = ChangeUser
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "id",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {"fields": ("avatar",)},
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {"fields": ("avatar",)},
        ),
    )


admin.site.register(CustomUser, NewMyUser)