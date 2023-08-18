from django.contrib import admin

from .models import Transactions, SavingScheme, TransactionEntries, SavingSchemeEntries


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "code"]
    list_filter = ["id", "code"]


@admin.register(SavingScheme)
class SavingSchemeAdmin(admin.ModelAdmin):
    list_display = ["id", "code"]
    list_filter = ["id", "code"]


@admin.register(SavingSchemeEntries)
class SavingSchemeEntriesAdmin(admin.ModelAdmin):
    list_display = ["id", "disbursement_type"]
    list_filter = ["id", "employee"]


@admin.register(TransactionEntries)
class TransactionEntriesAdmin(admin.ModelAdmin):
    list_display = ["id", "disbursement_type"]
    list_filter = ["id", "transaction_code"]
