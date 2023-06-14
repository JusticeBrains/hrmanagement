from rest_framework.routers import SimpleRouter

from .views import (
    EmployeeLeaveLimitsViewSet,
    LeaveLimitsViewSet,
    LeaveRequestViewSet,
    LeaveTypeViewSet,
    LeavePlanViewSet,
    HolidayCalenderViewset,
)

router = SimpleRouter()
router.register("leaverequest", LeaveRequestViewSet, basename="leaverequest")
router.register("leaveplan", LeavePlanViewSet, basename="leaveplan")
router.register("leavetype", LeaveTypeViewSet, basename="leavetype")
router.register("holidays", HolidayCalenderViewset, basename="holidays")
router.register("leavelimits", LeaveLimitsViewSet, basename="leavelimits")
router.register(
    "employeeleavelimits", EmployeeLeaveLimitsViewSet, basename="employeeleavelimits"
)

urlpatterns = router.urls
