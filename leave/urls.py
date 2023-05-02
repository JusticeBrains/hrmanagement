from rest_framework.routers import SimpleRouter

from .views import  LeaveRequestViewSet, LeaveTypeViewSet, LeavePlanViewSet

router = SimpleRouter()
router.register('leaverequest', LeaveRequestViewSet, basename='leaverequest')
router.register('leaveplan', LeavePlanViewSet, basename='leaveplan')
router.register('leavetype', LeaveTypeViewSet, basename='leavetype')


urlpatterns = router.urls
