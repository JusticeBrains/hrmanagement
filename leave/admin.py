from django.contrib import admin
from leave import models as lmodels


# admin.site.register(lmodels.LeaveRequest)
admin.site.register(lmodels.LeaveType)


@admin.register(lmodels.LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = [
        "start_date",
        "end_date",
        "days_left",
        "no_of_days_requested",
        "date_applied",
    ]


admin.site.register(lmodels.StaffCategory)
admin.site.register(lmodels.Department)
admin.site.register(lmodels.Unit)
admin.site.register(lmodels.Branch)
