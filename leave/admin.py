from django.contrib import admin
from leave import models as lmodels


admin.site.register(lmodels.Policy)
admin.site.register(lmodels.Assignment)
admin.site.register(lmodels.LeaveRequest)
admin.site.register(lmodels.LeaveTransaction)
admin.site.register(lmodels.LeavePlan)
admin.site.register(lmodels.LeaveType)

class LeavePlanAdmin(admin.ModelAdmin):
    class Meta:
        model = lmodels.LeavePlan
        list_display = ('emp_name', 'leave_description', 'start_date', 'end_date',)