
from rest_framework import viewsets

from .serializers import PeriodSerializer
from .models import Period


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    filterset_fields = ["id", "date", "month", "year"]