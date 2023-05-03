from django.contrib import admin

from employee import models as emodels

admin.site.register(emodels.Employee)
admin.site.register(emodels.StaffCategory)
admin.site.register(emodels.Branch)
admin.site.register(emodels.Unit)
admin.site.register(emodels.Department)
admin.site.register(emodels.Notch)
admin.site.register(emodels.PayCategoryList)
