from rest_framework import serializers
from . import models as med_model


class MedicalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_model.MedicalCode
        fields = "__all__"


class MedicalCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_model.MedicalCenters
        fields = "__all__"