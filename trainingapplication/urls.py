from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("course", views.CourseViewSet, basename='course')
router.register('coursedetail', views.CourseDetailViewSet, basename='coursedetail')
router.register('organizers', views.OrganizerViewSet, basename='organizers')
router.register('plan', views.PlanViewSet, basename='plan')
router.register('expense', views.ExpenseViewSet, basename='expense')
router.register('budget', views.BudgteViewSet, basename='budget')
router.register('request', views.RequestViewSet, basename='request')
router.register('feedback', views.FeedbackViewSet, basename='feedback')
router.register('participants', views.ParticipantsViewSet, basename='participant')

urlpatterns = router.urls
