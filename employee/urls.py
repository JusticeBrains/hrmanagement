from rest_framework.routers import SimpleRouter

from . import views as employee_views

router = SimpleRouter()
router.register('employee', employee_views.EmployeeViewSet, basename='employee')
router.register('employeeappraisal', employee_views.EmployeeAppraisalViewSet, basename='employeeappraisal')
# router.register('employeepromotion', employee_views.EmployeePromotionViewSet, basename='employeepromotion')
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
router.register('appraisalgrading', employee_views.AppraisalGradingViewSet, basename='appraisalgrading')
router.register('employeeappraisaldetail', employee_views.EmployeeAppraisalDetailViewSet, basename='employeeappraisaldetail')
router.register('paygroup', employee_views.PayGroupViewSet, basename="paygroup")
router.register('employeededuction', employee_views.EmployeeDeductionViewSet, basename="employeededuction")
router.register('kpi', employee_views.KPIViewSet, basename="kpi")
router.register('employeekra', employee_views.EmployeeKRAViewSet, basename="employeekra")

urlpatterns = router.urls
