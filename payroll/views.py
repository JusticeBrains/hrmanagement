from rest_framework import viewsets

from .models import Transactions, SavingScheme
from .serializers import TransactionSerializer, SavingSchemeSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class SavingSchemeViewSet(viewsets.ModelViewSet):
    queryset = SavingScheme.objects.all()
    serializer_class = SavingSchemeSerializer
