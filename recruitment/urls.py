
from rest_framework.routers import SimpleRouter
from .views import (
    AppicantQualifivationViewSet,
    JobApplicationViewSet,
    JobRequirementsViewSet,
    EmployeeRequisitionViewSet,
    InterviewscoreViewSet,
)

router = SimpleRouter()

router.register('applicantviewset', AppicantQualifivationViewSet, basename='applicantviewset')
router.register('jobapplication', JobApplicationViewSet, basename='jobapplication')
router.register('jobrequirements', JobRequirementsViewSet, basename='jobrequirements')
router.register('employeerequisition', EmployeeRequisitionViewSet, basename='employeerequisition')
router.register('interview', InterviewscoreViewSet, basename='interview')

urlpatterns = router.urls
