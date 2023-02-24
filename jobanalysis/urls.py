from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('jobanalysis', views.JobAnalysisViewSet, basename='jobanalysis')
router.register('jobanalysisduties', views.JobAnalysisDutiesViewSet, basename='jobanalysisduites')
router.register('jobrequirements', views.JobAnalysisRequirementViewSet, basename='jobrequirements')
router.register('jobanalysissupervision', views.JobAnalysisSupervisionViewSet, basename='jobanalysissupervision')
router.register('jobanalysiscontact', views.JobAnalysisContactViewSet, basename='jobanalysiscontact')
router.register('jobanalysisauthoritylimit', views.JobAnalysisAuthorityLimitViewSet,
                basename='jobanalysisauthoritylimit')
router.register('jobanalysisdemand', views.JobAnalysisDemandViewSet, basename='jobanalysisdemand')
router.register('jobanalysisrequirement', views.JobAnalysisRequirementViewSet, basename='jobanalysisrequirement')
router.register('jobevaluation', views.JobEvaluationViewSet, basename='jobevaluation')

urlpatterns = router.urls
