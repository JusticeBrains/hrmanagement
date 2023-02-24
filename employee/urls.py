from rest_framework.routers import SimpleRouter

from . import views as employee_views

router = SimpleRouter()
router.register('employee', employee_views.EmployeeViewSet, basename='employee')
router.register('appraisalareas', employee_views.AppraisalAreaViewSet, basename='appraisalarea')
router.register('employeeappraisal', employee_views.EmployeeAppraisalViewSet, basename='employeeappraisal')
router.register('employeeappraisalresponse', employee_views.EmployeeAppraisalResponseViewSet,
                basename='employeeappraisalresponse')
router.register('employeepromotion', employee_views.EmployeePromotionViewSet, basename='employeepromotion')
router.register('employeemedical', employee_views.EmployeeMedicalViewSet, basename='employeemedical')
router.register('employeedisciplinaryactions', employee_views.EmployeeDisciplinaryActionViewSet,
                basename='employeedisciplinaryactions')
router.register('employeepolicy', employee_views.EmployeePolicyViewSet, basename='employeepolicy')
router.register('employeepayreview', employee_views.EmployeePayReviewViewSet, basename='employeepayreview')

urlpatterns = router.urls
