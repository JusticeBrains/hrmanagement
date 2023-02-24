from rest_framework.routers import SimpleRouter

from .views import PayGroupViewSet

router = SimpleRouter()
router.register('paygroup', PayGroupViewSet, basename='paygroup')

urlpatterns = router.urls
