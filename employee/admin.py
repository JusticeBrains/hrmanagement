from django.contrib import admin

from employee import models as emodels


@admin.register(emodels.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["code", "company", "pay_group_code", "second_category_level"]
    list_display = [
        "fullname",
        "code",
        "company",
        "pay_group_code",
        "second_category_level",
    ]


@admin.register(emodels.PayGroup)
class PaygroupAdmin(admin.ModelAdmin):
    search_fields = ["no", "description", "company"]
    list_display = ["no", "company"]


@admin.register(emodels.EmployeeDeduction)
class EmployeeDeductionAdmin(admin.ModelAdmin):
    list_display = [
        "employee_name",
        "no_of_days",
    ]
    search_fields = ["employee_name", "no_of_days"]


@admin.register(emodels.EmployeeKRA)
class EmployeeKRAAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "total_score",
        "company",
    ]
    search_fields = [
        "name",
        "total_score",
        "company",
    ]


@admin.register(emodels.KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = [
        "employee_id",
        "employee_kra",
        "company",
    ]
    search_fields = [
        "employee_id",
        "employee_kra",
        "company",
    ]


@admin.register(emodels.EmployeeMedicalClaim)
class EmployeeMedicalClaim(admin.ModelAdmin):
    list_display = ["emp_name", "department", "company"]
    search_fields = ["emp_name", "department", "company"]


admin.site.register(emodels.StaffCategory)
admin.site.register(emodels.Branch)
admin.site.register(emodels.Unit)
admin.site.register(emodels.Department)
admin.site.register(emodels.Notch)
admin.site.register(emodels.AppraisalGrading)
admin.site.register(emodels.EmployeeAppraisal)
admin.site.register(emodels.PropertyAssignment)