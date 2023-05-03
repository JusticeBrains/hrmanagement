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
# router.register('employeepolicy', employee_views.EmployeePolicyViewSet, basename='employeepolicy')
router.register('employeepayreview', employee_views.EmployeePayReviewViewSet, basename='employeepayreview')
router.register('staff-category', employee_views.StaffCategoryViewSet, basename='staff-category')
router.register('department', employee_views.DepartmentViewSet, basename='department')
router.register('unit', employee_views.UnitViewSet, basename='unit')
router.register('branch', employee_views.BranchViewSet, basename='branch')
router.register('notch', employee_views.NotchViewSet, basename='branch')
router.register('paycategorylis', employee_views.PayCategoryListViewSet, basename='branch')

urlpatterns = router.urls
