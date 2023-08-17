from rest_framework.routers import SimpleRouter

from .views import (
    TransactionViewSet,
    SavingSchemeViewSet,
    TransactionEntriesViewSet,
    SavingSchemeEntriesViewSet,
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

urlpatterns = router.urls
