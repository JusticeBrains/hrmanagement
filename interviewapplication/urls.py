from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('interviewscoreguide', views.InterviewScoreViewSet, basename='interviewscoreguide')
router.register('interviewpanel', views.InterviewPanelViewSet, basename='interviewpanel')
router.register('interviewtestquestionnaire', views.InterviewTestQuestionnaireViewSet,
                basename='interviewtestquestionnaire')
router.register('medicalquestionnaire', views.MedicalQuestionnaireViewSet, basename='medicalquestionnaire')
router.register('applicationmedicaltest', views.ApplicationMedicalTestViewSet, basename='applicationmedicaltest')

urlpatterns = router.urls
