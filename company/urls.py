from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('company', views.CompanyViewSet, basename='company')
router.register('companytype', views.CompanyTypeViewSet, basename='companytype')
router.register('companyfield', views.CompanyFieldViewSet, basename='companyfield')
router.register('holiday', views.HolidayViewSet, basename='holiday')
router.register('medicalcodes', views.MedicalCodesViewSet, basename='medicalcodes')
router.register('medicalcentre', views.MedicalCentreViewSet, basename='medicalcentre')
router.register('property', views.PropertyViewSet, basename='property')
router.register('propertyassignment', views.PropertyAssignmentViewSet, basename='propertyassignment')
router.register('disciplinaryactions', views.DiscplinaryActionsViewSet, basename='disciplinaryactions')
router.register('job', views.JobViewSet, basename='job')
router.register('minimumqualification', views.MinimumQualificationViewSet, basename='minimumqualification')
router.register('qualificationmetricsqef', views.QualificationMetricSQEFViewSet, basename='qualificationmetricsqef')
router.register('jobopening', views.JobOpeningViewSet, basename='jobopening')
router.register('applicationpool', views.ApplicationPoolViewSet, basename='applicationpool')
router.register('shortlistedapplication', views.ShortListedApplicationViewSet, basename='shortlistedapplication')
router.register('applicationreference', views.ApplicationReferencesViewSet, basename='applicarionreference')
router.register('application', views.ApplicationQEViewSet, basename='applicationqe')
# router.register('jobapplication', views.JobApplicationViewSet, basename='jobapplication')
router.register('jobappplicationqualification', views.JobApplicationQualificationViewSet,
                basename='jobappplicationqualification')
router.register('hrneedssqef', views.HRNeedsSQEFViewSet, basename='hrneedssqef')
router.register('hrneedsline', views.HRNeedsLineViewSet, basename='hrneedsline')
router.register('hrapprovalentry', views.HRApprovalEntryViewSet, basename='hrapprovalentry')
router.register('hralerts', views.HRAlertsViewSet, basename='hralerts')
router.register('workmencompensation', views.WorkmenCompensationViewSet, basename='workmencompensation')
router.register('expatriates', views.ExpatriatesViewSet, basename='expatriates')
router.register('expatriatesapplication', views.ExpatriatesApplicationViewSet, basename='expatriatesapplication')
router.register('companystaffbreakdown', views.CompanyStaffBreakdownViewSet, basename='companystaffbreakdown')
router.register('passportissues', views.PassportIssuesViewSet, basename='passportissues')
router.register('performanceoverview', views.PerformanceOverviewViewSet, basename='performanceoverview')
router.register('organizationstructure', views.OrganizationStructureViewSet, basename='organizationstructure')
router.register('grievanceheader', views.GrievanceHeaderViewSet, basename='grievanceheader')
router.register('grievanceline', views.GrievanceLineViewSet, basename='grievanceline')
router.register('grievanceentry', views.GrievanceEntryViewSet, basename='grievanceentry')
router.register('grievancecommittemembers', views.GrievanceCommitteeMembersViewSet, basename='grievancecommittemembers')
router.register('travels', views.TravelsViewSet, basename='travels')
router.register('travelexpenses', views.TravelExpensesViewSet, basename='travelexpenses')
router.register('couriercompanies', views.CourierCompaniesViewSet, basename='grievancecommittemembers')
router.register('courierservicerequisition', views.CourierServiceRequisitionViewset,
                basename='courierservicerequisition')
router.register('hospitalityfacilities', views.HospitalityFacilitiesViewSet, basename='hospitalityfacilities')
router.register('hospitalityservices', views.HospitalityServicesViewSet, basename='hospitalityservices')
router.register('collectivebargaining', views.CollectiveBargainingViewSet, basename='collectivebargaining')
router.register('cbaissues', views.CBAIssuesViewSet, basename='cbaissues')
router.register('sjncmembers', views.SJNCMembersViewSet, basename='sjncmembers')
router.register('cashbenefitpayment', views.CashBenefitPaymentViewSet, basename='cashbenefitpayment')
router.register('endofserviceentry', views.EndOfServiceEntryViewSet, basename='endofserviceentry')
router.register('jobtitles', views.JobTitleViewSet, basename='jobtitles')
router.register('salarygrade', views.SalaryGradeViewSet, basename='salarygrade')

urlpatterns = router.urls
