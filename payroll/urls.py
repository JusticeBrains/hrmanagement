from rest_framework.routers import SimpleRouter

from .views import TransactionViewSet, SavingSchemeViewSet


router = SimpleRouter()

router.register("transaction", TransactionViewSet, basename="transaction")
router.register("saving-scheme", SavingSchemeViewSet, basename="saving-scheme")


urlpatterns = router.urls
