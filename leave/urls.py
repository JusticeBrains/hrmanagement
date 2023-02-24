from rest_framework.routers import SimpleRouter

from .views import LeavePlanViewSet, AssignmentViewSet, LeaveRequestViewSet, LeaveTransactionViewSet

router = SimpleRouter()
router.register('leaverequest', LeaveRequestViewSet, basename='leaverequest')
router.register('assignment', AssignmentViewSet, basename='assignment')
router.register('leave-plan', LeavePlanViewSet, basename='leaveplan')
router.register('leavetransaction', LeaveTransactionViewSet, basename='leavetransaction')

urlpatterns = router.urls
