from rest_framework.routers import SimpleRouter

from .views import  LeaveRequestViewSet, LeaveTypeViewSet

router = SimpleRouter()
router.register('leaverequest', LeaveRequestViewSet, basename='leaverequest')
router.register('leavetype', LeaveTypeViewSet, basename='leavetype')


urlpatterns = router.urls
