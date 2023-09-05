from rest_framework import viewsets

from .models import (
    AuditTrail,
    EmployeeSavingSchemeEntries,
    EmployeeShiftEntries,
    EmployeeTransactionEntries,
    LoanEntries,
    Loans,
    Paymaster,
    ShiftEntries,
    ShiftSetUp,
    TaxLawType,
    TaxLaws,
    TaxRelief,
    Transactions,
    SavingScheme,
    SavingSchemeEntries,
    TransactionEntries,
    PayrollFormular,
    OvertimeSetup,
    OvertimeEntries,
)
from .serializers import (
    AuditTrailSerializer,
    EmployeeSavingSchemeEntriesSerializer,
    EmployeeShiftEntriesSerializer,
    EmployeeTransactionEntriesSerializer,
    LoanEntriesSerializer,
    LoansSerializer,
    PaymasterSerializer,
    ShiftEntriesSerializer,
    ShiftSetUpSerializer,
    TaxLawTypeSerializer,
    TaxLawsSerializer,
    TaxReliefSerializer,
    TransactionSerializer,
    SavingSchemeSerializer,
    SavingSchemeEntriesSerializer,
    TransactionEntriesSerializer,
    PayrollFormularSerializer,
    OvertimeSerializer,
    OvertimeEntriesSerializer,
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


class LoansViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    filterset_fields = "__all__"


class LoanEntriesViewSet(viewsets.ModelViewSet):
    queryset = LoanEntries.objects.all()
    serializer_class = LoanEntriesSerializer
    filterset_fields = [
        "id",
        "loan",
        "loan_name",
        "description",
        "amount",
        "employee",
        "employee_code",
        "employee_name",
        "monthly_repayment",
        "total_amount_paid",
        "duration",
        "company",
        "company_name",
        "status",
        "created_at",
        "transaction_period",
        "transaction_period_code",
        "deduction_start_period",
        "deduction_start_period_code",
        "deduction_end_period",
        "deduction_end_period_code",
        "user_id",
    ]


class AuditTrailViewSet(viewsets.ModelViewSet):
    queryset = AuditTrail.objects.all()
    serializer_class = AuditTrailSerializer
    filterset_fields = "__all__"


class EmployeeSavingSchemeEntriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeSavingSchemeEntries.objects.all()
    serializer_class = EmployeeSavingSchemeEntriesSerializer
    filterset_fields = "__all__"


class EmployeeTransactionEntriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeTransactionEntries.objects.all()
    serializer_class = EmployeeTransactionEntriesSerializer
    filterset_fields = "__all__"


class ShiftSetUpViewSet(viewsets.ModelViewSet):
    queryset = ShiftSetUp.objects.all()
    serializer_class = ShiftSetUpSerializer
    filterset_fields = "__all__"


class ShiftEntriesViewSet(viewsets.ModelViewSet):
    queryset = ShiftEntries.objects.all()
    serializer_class = ShiftEntriesSerializer
    filterset_fields = "__all__"


class EmployeeShiftEntriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeShiftEntries.objects.all()
    serializer_class = EmployeeShiftEntriesSerializer
    filterset_fields = "__all__"


class PaymasterViewSet(viewsets.ModelViewSet):
    queryset = Paymaster.objects.all()
    serializer_class = PaymasterSerializer
    filterset_fields = "__all__"


class TaxLawsViewSet(viewsets.ModelViewSet):
    queryset = TaxLaws.objects.all()
    serializer_class = TaxLawsSerializer
    filterset_fields = "__all__"


class TaxLawTypeViewSet(viewsets.ModelViewSet):
    queryset = TaxLawType.objects.all()
    serializer_class = TaxLawTypeSerializer
    filterset_fields = "__all__"


class TaxReliefViewSet(viewsets.ModelViewSet):
    queryset = TaxRelief.objects.all()
    serializer_class = TaxReliefSerializer
    filterset_fields = "__all__"
