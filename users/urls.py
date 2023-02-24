from rest_framework.routers import SimpleRouter

from .views import UserViewset

router = SimpleRouter()
router.register('', UserViewset, basename='users')

urlpatterns = router.urls
