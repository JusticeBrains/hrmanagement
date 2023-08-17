from rest_framework import viewsets
from django_property_filter import PropertyNumberFilter, PropertyFilterSet

from .serializers import PeriodSerializer, PeriodYearSerializer
from .models import Period, PeriodYear


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    # filterset_fields = [
    #     "id",
    #     "period_year",
    #     "total_working_days",
    #     "total_working_hours",
    #     "start_date",
    #     "end_date",
    #     "no_of_days",
    #     "period_name",
    #     "period_code",
    # ]


class PeriodYearViewSet(viewsets.ModelViewSet):
    queryset = PeriodYear.objects.all()
    serializer_class = PeriodYearSerializer
    filterset_fields = "__all__"
