
from rest_framework.routers import SimpleRouter
from .views import (
    AppicantViewSet,
    JobApplicationViewSet,
    JobRequirementsViewSet,
    EmployeeRequisitionViewSet,
    InterviewscoreViewSet,
)

router = SimpleRouter()

router.register('applicantviewset', AppicantViewSet, basename='applicantviewset')
router.register('jobapplication', JobApplicationViewSet, basename='jobapplication')
router.register('jobrequirements', JobRequirementsViewSet, basename='jobrequirements')
router.register('employeerequisition', EmployeeRequisitionViewSet, basename='employeerequisition')
router.register('interview', InterviewscoreViewSet, basename='interview')

urlpatterns = router.urls
