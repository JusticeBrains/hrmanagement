from django.contrib import admin

from .models import Transactions, SavingScheme, TransactionEntries, SavingSchemeEntries, OvertimeEntries


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", ]
    list_filter = ["id",]


@admin.register(SavingScheme)
class SavingSchemeAdmin(admin.ModelAdmin):
    list_display = ["id",]
    list_filter = ["id", ]


@admin.register(SavingSchemeEntries)
class SavingSchemeEntriesAdmin(admin.ModelAdmin):
    list_display = ["id", "disbursement_type"]
    list_filter = ["id", "employee"]


@admin.register(TransactionEntries)
class TransactionEntriesAdmin(admin.ModelAdmin):
    list_display = ["id", "disbursement_type"]
    list_filter = ["id", "transaction_code"]


@admin.register(OvertimeEntries)
class OverTimeEntriesAdmin(admin.ModelAdmin):
    ...
