from rest_framework import serializers

from .models import (InsurancePremiumPayments,
                     GroupLifeInsurance,
                     GroupInsuranceBeneficiaries,
                     TravelInsuranceEntry
                     )


class InsurancePremiumPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePremiumPayments
        fields = "__all__"


class GroupLifeInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupLifeInsurance
        fields = "__all__"


class GroupInsuranceBeneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupInsuranceBeneficiaries
        fields = "__all__"


class TravelInsuranceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelInsuranceEntry
        fields = "__all__"
