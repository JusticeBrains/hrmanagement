from django.contrib import admin

from .models import Company, CompanyType, JobTitles, SalaryGrade


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias',)
    search_fields = ["name"]

@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(JobTitles)
class JobTitlesAdmin(admin.ModelAdmin):
    list_display = ('code','description', 'company')
admin.site.register(SalaryGrade)
