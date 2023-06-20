from rest_framework.routers import SimpleRouter

from . import views as employee_views

router = SimpleRouter()
router.register("employee", employee_views.EmployeeViewSet, basename="employee")
router.register(
    "employeeappraisal",
    employee_views.EmployeeAppraisalViewSet,
    basename="employeeappraisal",
)
# router.register('employeepromotion', employee_views.EmployeePromotionViewSet, basename='employeepromotion')
router.register(
    "employeemedicalclaim",
    employee_views.EmployeeMedicalClaimViewSet,
    basename="employeemedicalclaim",
)
router.register(
    "employeedisciplinaryactions",
    employee_views.EmployeeDisciplinaryActionViewSet,
    basename="employeedisciplinaryactions",
)
# router.register('employeepolicy', employee_views.EmployeePolicyViewSet, basename='employeepolicy')
router.register(
    "employeepayreview",
    employee_views.EmployeePayReviewViewSet,
    basename="employeepayreview",
)
router.register(
    "staffcategory", employee_views.StaffCategoryViewSet, basename="staff-category"
)
router.register("department", employee_views.DepartmentViewSet, basename="department")
router.register("unit", employee_views.UnitViewSet, basename="unit")
router.register("branch", employee_views.BranchViewSet, basename="branch")
router.register("notch", employee_views.NotchViewSet, basename="branch")
router.register(
    "appraisal-grading",
    employee_views.AppraisalGradingViewSet,
    basename="appraisal-dgrading",
)
router.register("paygroup", employee_views.PayGroupViewSet, basename="paygroup")
router.register(
    "employeededuction",
    employee_views.EmployeeDeductionViewSet,
    basename="employee-deduction",
)
router.register("kpi", employee_views.KPIViewSet, basename="kpi")
router.register(
    "employee-kra", employee_views.EmployeeKRAViewSet, basename="employee-kra"
)
router.register(
    "property-assignment",
    employee_views.PropertyAssignmentViewSet,
    basename="propertya-ssignment",
)
router.register(
    "property-request",
    employee_views.PropertyRequestViewSet,
    basename="property-request",
)
router.register(
    "supervisor-rating-guide",
    employee_views.SupervisorRatingGuideViewSet,
    basename="supervisor-rating-guide",
)
router.register(
    "behavioural-rating-guide",
    employee_views.BehaviourialRatingGuideViewSet,
    basename="behavioural-rating-guide",
)
router.register(
    "behavioural-competencies",
    employee_views.BehavourialCompetenciesViewSet,
    basename="behavioural-competencies",
)
router.register(
    "employee-behavioural",
    employee_views.EmployeeBehaviouralViewSet,
    basename="employee-behavoural",
)
urlpatterns = router.urls
