from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# User = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "emp_code",)
    list_filter = ("email", "emp_code",)
    fieldsets = (
        ("User", {"fields": ("email", "password", "is_admin", "username","companies","first_name","last_name","employee_id",)}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active","groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "employee_id",
                    "emp_code",
                    "is_admin",
                    "password1",
                    "password2",
                    "companies",
                    "is_staff",
                    "is_active",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email", "emp_code")
    ordering = ("email", "emp_code")