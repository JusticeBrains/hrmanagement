from django.contrib import admin

from .models import (
    EmployeeLoanPayment,
    EmployeeSavingSchemeEntries,
    EmployeeShiftEntries,
    EmployeeTransactionEntries,
    Paymaster,
    ShiftEntries,
    ShiftSetUp,
    Transactions,
    SavingScheme,
    TransactionEntries,
    SavingSchemeEntries,
    OvertimeEntries,
    OvertimeSetup,
    LoanEntries,
    Loans,
    AuditTrail,
)


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]
    list_filter = [
        "id",
    ]


@admin.register(SavingScheme)
class SavingSchemeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]
    list_filter = [
        "id",
    ]


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


@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    ...


@admin.register(LoanEntries)
class LoanEntriesAdmin(admin.ModelAdmin):
    list_display = [
        "loan",
        "amount",
        "employee_name",
        "monthly_repayment",
        "duration",
        "total_amount_paid",
    ]


@admin.register(AuditTrail)
class AuditTrailAdmin(admin.ModelAdmin):
    ...


@admin.register(EmployeeSavingSchemeEntries)
class EmployeeSavingSchemeEntriesAdmin(admin.ModelAdmin):
    ...


@admin.register(EmployeeTransactionEntries)
class EmployeeTransactionEntriesAdmin(admin.ModelAdmin):
    list_display = [
        "employee_name",
        "transaction_entry",
        "transaction_type",
        "amount",
        "company_name",
    ]
    search_fields = [
        "employee_name",
        "company_name",
        "transaction_type",
        "employee_code",
    ]


@admin.register(ShiftSetUp)
class ShiftSetUpEntriesAdmin(admin.ModelAdmin):
    ...


@admin.register(ShiftEntries)
class ShiftEntriesAdmin(admin.ModelAdmin):
    ...


@admin.register(EmployeeShiftEntries)
class EmployeeShiftEntriesAdmin(admin.ModelAdmin):
    ...


@admin.register(OvertimeSetup)
class OvertimeSetupAdmin(admin.ModelAdmin):
    ...


@admin.register(Paymaster)
class PaymasterAdmin(admin.ModelAdmin):
    list_display = [
        "employee_name",
        "employee_code",
        "basic_salary",
        "allowances",
        "deductions",
        "period_name",
    ]
    search_fields = ["employee_code"]


class EmployeeLoanPayment(admin.ModelAdmin):
    list_display = ["loan_name", "amount", "employee_code", "employee_name"]
    search_fields = ["employee_code","employee_name"]