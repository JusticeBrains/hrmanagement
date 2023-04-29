from rest_framework.routers import SimpleRouter

from .views import  LeaveRequestViewSet

router = SimpleRouter()
router.register('leaverequest', LeaveRequestViewSet, basename='leaverequest')

urlpatterns = router.urls
