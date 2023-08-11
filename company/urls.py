from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('company', views.CompanyViewSet, basename='company')
router.register('companytype', views.CompanyTypeViewSet, basename='companytype')
router.register('holiday', views.HolidayViewSet, basename='holiday')
router.register('jobtitles', views.JobTitleViewSet, basename='jobtitles')
router.register('salarygrade', views.SalaryGradeViewSet, basename='salarygrade')
router.register('bank', views.BankViewSet, basename='bank')
router.register('bank-branch', views.BankBranchViewSet, basename='bank-branch')

urlpatterns = router.urls
