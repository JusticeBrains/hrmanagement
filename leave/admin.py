from django.contrib import admin
from leave import models as lmodels


admin.site.register(lmodels.LeaveRequest)
admin.site.register(lmodels.LeaveType)

class LeavePlanAdmin(admin.ModelAdmin):
    class Meta:
        model = lmodels.LeaveRequest
        list_display = ('leave_description', 'start_date', 'end_date',)