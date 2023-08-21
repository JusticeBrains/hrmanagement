from rest_framework import viewsets

from .models import (
    Transactions,
    SavingScheme,
    SavingSchemeEntries,
    TransactionEntries,
    PayrollFormular,
    OvertimeSetup,
    OvertimeEntries
)
from .serializers import (
    TransactionSerializer,
    SavingSchemeSerializer,
    SavingSchemeEntriesSerializer,
    TransactionEntriesSerializer,
    PayrollFormularSerializer,
    OvertimeSerializer,
    OvertimeEntriesSerializer
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


class PayrollFormularViewSet(viewsets.ModelViewSet):
    queryset = PayrollFormular.objects.all()
    serializer_class = PayrollFormularSerializer
    filterset_fields = "__all__"


class OvertimeSetupViewSet(viewsets.ModelViewSet):
    queryset = OvertimeSetup.objects.all()
    serializer_class = OvertimeSerializer
    filterset_fields = "__all__"

class OvertimeEntriesViewSet(viewsets.ModelViewSet):
    queryset = OvertimeEntries.objects.all()
    serializer_class = OvertimeEntriesSerializer
    filterset_fields = "__all__"