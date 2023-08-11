from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Company, CompanyType, JobTitles, SalaryGrade, Bank, BankBranch


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


class BankAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = (
        "id",
        "name",
    )
    search_fields = ("id", "name",)

class BankBranchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = (
        "id",
        "name",
    )
    list_display = (
        "id",
        "name",
        "bank",
    )
    search_fields = ("id", "name",)

admin.site.register(SalaryGrade)


admin.site.register(BankBranch, BankBranchAdmin)
admin.site.register(Bank, BankAdmin)
