from django.contrib import admin
from leave import models as lmodels


# admin.site.register(lmodels.LeaveRequest)
admin.site.register(lmodels.LeaveType)
admin.site.register(lmodels.HolidayCalender)
admin.site.register(lmodels.EmployeeLeaveLimits)
admin.site.register(lmodels.LeaveLimits)

@admin.register(lmodels.LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = [
        "employee",
        "emp_code",
        "start_date",
        "end_date",
        'resumption_date',
        "no_of_days_requested",
        "date_applied",
        'is_extend',
        'no_of_extension_days',
        'extension_date',
        'hr_extension_status',
    ]

@admin.register(lmodels.LeavePlan)
class LeavePlanAdmin(admin.ModelAdmin):
    list_display = [
        "employee",
        "emp_code",
        "start_date",
        "end_date",
        'resumption_date',
        "no_of_days_requested",
        "date_applied",
    ]

