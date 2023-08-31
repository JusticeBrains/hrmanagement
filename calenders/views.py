from rest_framework import viewsets
from django_property_filter import PropertyNumberFilter, PropertyFilterSet

from .serializers import PeriodSerializer, PeriodYearSerializer, GlobalInputsSerializer
from .models import Period, PeriodYear, GlobalInputs


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all().order_by("period_year__year", "month")
    serializer_class = PeriodSerializer
    filterset_fields = [
        "id",
        "period_year",
        "total_working_days",
        "period_year_value",
        "total_working_hours",
        "start_date",
        "end_date",
        "no_of_days",
        "period_name",
        "period_code",
        "status",
        "process",
        "company",
    ]


class PeriodYearViewSet(viewsets.ModelViewSet):
    queryset = PeriodYear.objects.all()
    serializer_class = PeriodYearSerializer
    filterset_fields = "__all__"


class GlobalInputViewSet(viewsets.ModelViewSet):
    queryset = GlobalInputs.objects.all()
    serializer_class = GlobalInputsSerializer
    filterset_fields = "__all__"
