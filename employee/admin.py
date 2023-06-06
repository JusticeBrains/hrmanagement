from django.contrib import admin

from employee import models as emodels

@admin.register(emodels.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['code', 'company', 'pay_group_code']
    list_display = ['fullname','code', 'company', 'pay_group_code']


@admin.register(emodels.EmployeeAppraisalDetail)
class EmployeeAppraisalDetailAdmin(admin.ModelAdmin):
    list_display = ['emp_code', 'period', 'emp_name', 'score']


@admin.register(emodels.PayGroup)
class PaygroupAdmin(admin.ModelAdmin):
    search_fields = ['no','description', 'company']
    list_display = ["no","company"]

admin.site.register(emodels.StaffCategory)
admin.site.register(emodels.Branch)
admin.site.register(emodels.Unit)
admin.site.register(emodels.Department)
admin.site.register(emodels.Notch)
admin.site.register(emodels.AppraisalGrading)
admin.site.register(emodels.EmployeeAppraisal)