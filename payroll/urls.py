from rest_framework.routers import SimpleRouter

from .views import (
    TransactionViewSet,
    SavingSchemeViewSet,
    TransactionEntriesViewSet,
    SavingSchemeEntriesViewSet,
    PayrollFormularViewSet,
    OvertimeSetupViewSet,
    OvertimeEntriesViewSet
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
router.register('overtime-entries', OvertimeEntriesViewSet, basename="overtime-entries")
urlpatterns = router.urls
OvertimeEntriesViewSet