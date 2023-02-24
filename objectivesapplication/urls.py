from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('corporatevalue', views.CorporateValueViewSet, basename='corporatevalue')
router.register('cooperateobjective', views.CooperateObjectiveViewSet, basename='cooperateobjective')
router.register('departmentobjective', views.DepartmentObjectiveViewSet, basename='departmentobjective')
router.register('objectivereviewline', views.ObjectiveReviewLinesViewSet, basename='objectivereviewline')
router.register('individualobjectiveline', views.IndividualObjectiveLineViewSet, basename='individualobjectiveline')
router.register('individualobjectivesetting', views.IndividualObjectiveSettingViewSet,
                basename='individualobjectivesetting')
router.register('individualobjectivereview', views.IndividualObjectiveReviewViewSet,
                basename='individualobjectivereview')

urlpatterns = router.urls
