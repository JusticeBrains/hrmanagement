from django.contrib import admin

from employee import models as emodels

@admin.register(emodels.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['code', 'company']
    list_display = ['fullname','code', 'company']


@admin.register(emodels.EmployeeAppraisalDetail)
class EmployeeAppraisalDetailAdmin(admin.ModelAdmin):
    list_display = ['emp_code', 'period', 'emp_name', 'score']

admin.site.register(emodels.StaffCategory)
admin.site.register(emodels.Branch)
admin.site.register(emodels.Unit)
admin.site.register(emodels.Department)
admin.site.register(emodels.Notch)
admin.site.register(emodels.PayCategoryList)
admin.site.register(emodels.AppraisalGrading)
admin.site.register(emodels.EmployeeAppraisal)