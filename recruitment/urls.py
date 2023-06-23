from rest_framework.routers import SimpleRouter
from .views import (
    AppicantQualifivationViewSet,
    CompanyQualificationsViewSet,
    GlobalQualificationViewSet,
    JobApplicationViewSet,
    EmployeeRequisitionViewSet,
    InterviewscoreViewSet,
)

router = SimpleRouter()

router.register(
    "applicantviewset", AppicantQualifivationViewSet, basename="applicantviewset"
)
router.register("jobapplication", JobApplicationViewSet, basename="jobapplication")
router.register(
    "employeerequisition", EmployeeRequisitionViewSet, basename="employeerequisition"
)
router.register("interview", InterviewscoreViewSet, basename="interview")
router.register(
    "global-qualifcations", GlobalQualificationViewSet, basename="global-qualifcation"
)
router.register(
    "company-qualification",
    CompanyQualificationsViewSet,
    basename="company-qualification",
)

urlpatterns = router.urls
