from django.contrib import admin

from .models import Company, CompanyType, Job, JobTitles, SalaryGrade


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias',)
    search_fields = ["name"]

@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('comp_code', 'job_code','job_title',)


admin.site.register(JobTitles)
admin.site.register(SalaryGrade)
