from django.contrib import admin

from employee import models as emodels

admin.site.register(emodels.Employee)
admin.site.register(emodels.StaffCategory)
