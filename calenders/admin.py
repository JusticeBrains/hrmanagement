from django.contrib import admin

from .models import Period, PeriodYear, GlobalInputs

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    ...

admin.site.register(PeriodYear)
admin.site.register(GlobalInputs)