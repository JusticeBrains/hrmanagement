from django.contrib import admin
from leave import models as lmodels


# admin.site.register(lmodels.LeaveRequest)
admin.site.register(lmodels.LeaveType)


@admin.register(lmodels.LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = [
        "employee",
        "emp_code",
        "start_date",
        "end_date",
        "no_of_days_requested",
        'no_of_days_left',
        "date_applied",
    ]

@admin.register(lmodels.LeavePlan)
class LeavePlanAdmin(admin.ModelAdmin):
    list_display = [
        "employee",
        "emp_code",
        "start_date",
        "end_date",
        "no_of_days_requested",
        'no_of_days_left',
        "date_applied",
    ]
