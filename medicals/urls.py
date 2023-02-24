from rest_framework.routers import SimpleRouter

from . import views 

router = SimpleRouter()
router.register('medicalcode', views.MedicalCodeViewSet, basename='medicalcode')
router.register('medicalcenter', views.MedicalCenterViewSet, basename='medicalcenter')

urlpatterns = router.urls
