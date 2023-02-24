from . import serializers as med_serializer
from . import models as medical_model

from rest_framework import viewsets


class MedicalCodeViewSet(viewsets.ModelViewSet):
    queryset = medical_model.MedicalCode.objects.all()
    serializer_class = med_serializer.MedicalCodeSerializer


class MedicalCenterViewSet(viewsets.ModelViewSet):
    queryset = medical_model.MedicalCenters.objects.all()
    serializer_class = med_serializer.MedicalCentersSerializer
