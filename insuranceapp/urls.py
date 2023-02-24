from rest_framework.routers import SimpleRouter

from .views import GroupInsuranceBeneficiariesViewSet, TravelInsuranceEntryViewSet, InsurancePremiumPaymentViewSet, \
    GroupLifeInsuranceViewSet

router = SimpleRouter()
router.register('groupinsurancebeneficiaries', GroupInsuranceBeneficiariesViewSet,
                basename='groupinsurancebeneficiaries')
router.register('travelinsuranceentry', TravelInsuranceEntryViewSet, basename='travelinsuranceentry')
router.register('insurancepremiumpayment', InsurancePremiumPaymentViewSet, basename='insurancepremium')
router.register('grouplifeinsurance', GroupLifeInsuranceViewSet, basename='grouplifeinsurance')

urlpatterns = router.urls
