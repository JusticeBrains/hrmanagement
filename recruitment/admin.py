from django.contrib import admin
from .models import (
    EmployeeRequisition,
    JobRequirements,
    JobApplication,
    ApplicantQualification,
    Interview,
)

@admin.register(EmployeeRequisition)
class EmployeeRequisitionAdmin(admin.ModelAdmin):
    list_display = [
        'department',
        'position',
        'no_of_vacancies'
    ]
    list_filter = ['department', 'position']
    search_fields = ['department', 'position']
    list_per_page = 50

@admin.register(JobRequirements)
class JobRequirementAdmin(admin.ModelAdmin):
    list_display = [
        'employee_requisition',
        'requirement_name',
        'description'
    ]
    list_filter = ['requirement_name']
    search_fields = ['requirement_name']
    list_per_page = 50

@admin.register(JobApplication)
class JobApplication(admin.ModelAdmin):
    list_display = [
        'employee_requisition',
        'fullname',
        'status',
        'short_list',
        'total_interview_score',
    ]
    list_filter = ['status','total_interview_score']
    search_fields = ['status',]
    list_per_page = 50


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ['panelist_name', 'interview_date', 'interview_time','interview_score']


@admin.register(ApplicantQualification)
class ApplicationQualificationAdmin(admin.ModelAdmin):
    list_display = ['qualification_name',]