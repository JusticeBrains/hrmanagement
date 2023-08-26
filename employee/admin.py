from django.contrib import admin

from employee import models as emodels


@admin.register(emodels.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["code", "company", "pay_group_name","company_email",""]
    list_display = [
        "fullname",
        "code",
        "company",
        "pay_group_name",
        "department_name",
        "branch_name",
        "is_hr",
        "company_email",
        "total_medical_claim_amount",
        "notch",
        "salary_grade",
    ]


@admin.register(emodels.PayGroup)
class PaygroupAdmin(admin.ModelAdmin):
    search_fields = ["description", "company"]
    list_display = ["company"]


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


@admin.register(emodels.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "company"]
    search_fields = ["code", "name"]

@admin.register(emodels.Unit)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "company","department"]
    search_fields = ["code", "name"]


@admin.register(emodels.Notch)
class NotchAdmin(admin.ModelAdmin):
    list_display = ["payroll_structure_code", 'no',"salary_grade", "company","amount"]
    search_fields = ["no"]

admin.site.register(emodels.StaffCategory)
admin.site.register(emodels.Branch)
admin.site.register(emodels.AppraisalGrading)
admin.site.register(emodels.EmployeeAppraisal)
admin.site.register(emodels.PropertyAssignment)
admin.site.register(emodels.PropertyRequest)
admin.site.register(emodels.SupervisorRatingGuide)
admin.site.register(emodels.BehaviourialRatingGuide)
admin.site.register(emodels.BehaviouralCompetencies)
admin.site.register(emodels.EmployeeBehavioural)