from rest_framework.routers import SimpleRouter

from .views import (
    AuditTrailViewSet,
    EmployeeSavingSchemeEntriesViewSet,
    EmployeeShiftEntriesViewSet,
    EmployeeTransactionEntriesViewSet,
    LoanEntriesViewSet,
    LoansViewSet,
    PaymasterViewSet,
    ShiftEntriesViewSet,
    ShiftSetUpViewSet,
    TaxLawsViewSet,
    TransactionViewSet,
    SavingSchemeViewSet,
    TransactionEntriesViewSet,
    SavingSchemeEntriesViewSet,
    PayrollFormularViewSet,
    OvertimeSetupViewSet,
    OvertimeEntriesViewSet,
)


router = SimpleRouter()

router.register("transaction", TransactionViewSet, basename="transaction")
router.register("saving-scheme", SavingSchemeViewSet, basename="saving-scheme")
router.register(
    "saving-scheme-entries",
    SavingSchemeEntriesViewSet,
    basename="saving-scheme-entries",
)
router.register(
    "transaction-entries", TransactionEntriesViewSet, basename="transaction-entries"
)
router.register("payroll-formular", PayrollFormularViewSet, basename="payroll-formular")
router.register("overtime-setup", OvertimeSetupViewSet, basename="overtime-setup")
router.register("overtime-entries", OvertimeEntriesViewSet, basename="overtime-entries")
router.register("loans", LoansViewSet, basename="loans")
router.register("loan-entries", LoanEntriesViewSet, basename="loans-entries")
router.register(
    "employee-transaction-entries",
    EmployeeTransactionEntriesViewSet,
    basename="employee-transaction-entries",
)
router.register(
    "employee-saving-scheme-entries",
    EmployeeSavingSchemeEntriesViewSet,
    basename="employee-saving-scheme-entries",
)
router.register("audit-trails", AuditTrailViewSet, basename="audit-trails")
router.register("shift-setup", ShiftSetUpViewSet, basename="shift-setup")
router.register("shift-entries", ShiftEntriesViewSet, basename="shift-entries")
router.register(
    "employee-shift-entries",
    EmployeeShiftEntriesViewSet,
    basename="employee-shift-entries",
)
router.register(
    "paymaster",
    PaymasterViewSet,
    basename="paymaster",
)
router.register(
    "tax-laws",
    TaxLawsViewSet,
    basename="tax-laws",
)
urlpatterns = router.urls
