from django.contrib import admin

from .models import Company, CompanyType, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('comp_name', 'comp_type','address','phone_number','contact_email')

@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'type')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('comp_code', 'job_code','job_title',)
