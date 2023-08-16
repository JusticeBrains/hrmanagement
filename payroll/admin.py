from django.contrib import admin

from .models import Transactions, SavingScheme

@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "code"]
    list_filter = ["id", "code"]

@admin.register(SavingScheme)
class SavingSchemeAdmin(admin.ModelAdmin):
    list_display = ["id", "code"]
    list_filter = ["id", "code"]