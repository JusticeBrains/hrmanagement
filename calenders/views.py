
from rest_framework import viewsets
from django_property_filter import PropertyNumberFilter, PropertyFilterSet

from .serializers import PeriodSerializer
from .models import Period

class PeriodFilter(PropertyFilterSet):
    month = PropertyNumberFilter(field_name="month")
    year = PropertyNumberFilter(field_name="year")

    class Meta:
        model = Period
        fields = ["id", "date", "month", "year"]

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    filterset_class = PeriodFilter