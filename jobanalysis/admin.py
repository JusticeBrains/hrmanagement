from django.contrib import admin

from .models import (
    JobAnalysis, 
    JobAnalysisAuthorityLimit,
    JobAnalysisContact, 
    JobAnalysisDemand,
    JobAnalysisDuties,
    JobAnalysisRequirement,
    JobAnalysisSupervision,
    JobEvaluation,
    JobRequirements,
)


@admin.register(JobAnalysis)
class JobAnalysisAdmin(admin.ModelAdmin):
    fields = ('emp_code', 'emp_name', 'job_title_code')

admin.site.register(JobAnalysisAuthorityLimit)
admin.site.register(JobAnalysisContact)
admin.site.register(JobAnalysisDemand)
admin.site.register(JobAnalysisDuties)
admin.site.register(JobAnalysisRequirement)
admin.site.register(JobAnalysisSupervision)
admin.site.register(JobEvaluation)
admin.site.register(JobRequirements)

