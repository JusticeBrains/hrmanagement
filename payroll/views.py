from rest_framework import viewsets

from .models import Transactions, SavingScheme, SavingSchemeEntries, TransactionEntries
from .serializers import (
    TransactionSerializer,
    SavingSchemeSerializer,
    SavingSchemeEntriesSerializer,
    TransactionEntriesSerializer,
)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = "__all__"


class SavingSchemeViewSet(viewsets.ModelViewSet):
    queryset = SavingScheme.objects.all()
    serializer_class = SavingSchemeSerializer
    filterset_fields = "__all__"


class SavingSchemeEntriesViewSet(viewsets.ModelViewSet):
    queryset = SavingSchemeEntries.objects.all()
    serializer_class = SavingSchemeEntriesSerializer
    filterset_fields = "__all__"


class TransactionEntriesViewSet(viewsets.ModelViewSet):
    queryset = TransactionEntries.objects.all()
    serializer_class = TransactionEntriesSerializer
    filterset_fields = "__all__"
