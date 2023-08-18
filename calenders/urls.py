from rest_framework.routers import SimpleRouter
from .views import PeriodViewSet, PeriodYearViewSet

router = SimpleRouter()

router.register("period", PeriodViewSet, basename="period")
router.register("period-year", PeriodYearViewSet, basename="period-year")

urlpatterns = router.urls
