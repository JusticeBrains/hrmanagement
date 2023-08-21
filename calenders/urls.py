from rest_framework.routers import SimpleRouter
from .views import PeriodViewSet, PeriodYearViewSet,GlobalInputViewSet

router = SimpleRouter()

router.register("period", PeriodViewSet, basename="period")
router.register("period-year", PeriodYearViewSet, basename="period-year")
router.register('global-inputs', GlobalInputViewSet, basename="global-inputs")
urlpatterns = router.urls
