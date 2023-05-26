from django.contrib import admin
from .models import (
    EmployeeRequisition,
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


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    if JobApplication.fullname:
        list_display = [
            'employee_requisition',
            'fullname',
            'status',
            'short_list',
            'total_interview_score',
        ]
    else:
        list_display = [
            'employee_requisition',
            'status',
            'short_list',
            'total_interview_score',
        ]
    list_filter = ['status','total_interview_score']
    search_fields = ['status',]
    list_per_page = 50


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    if Interview.job_application:
        list_display = ['job_application','panelist_name', 'interview_date', 'interview_time','interview_score']
    else:
        list_display = ['panelist_name', 'interview_date', 'interview_time','interview_score']



@admin.register(ApplicantQualification)
class ApplicationQualificationAdmin(admin.ModelAdmin):
    if ApplicantQualification.job_application:
        list_display = ['job_application','qualification_name',]
    else:
        list_display = ['qualification_name',]
