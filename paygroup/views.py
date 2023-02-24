from .models import PayGroup
from .serializers import PayGroupSerializer

from rest_framework import viewsets


class PayGroupViewSet(viewsets.ModelViewSet):
    queryset = PayGroup.objects.all()
    serializer_class = PayGroupSerializer
