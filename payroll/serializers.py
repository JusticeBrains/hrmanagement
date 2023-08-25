from rest_framework import serializers

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
    Transactions,
    SavingScheme,
    SavingSchemeEntries,
    TransactionEntries,
    PayrollFormular,
    OvertimeSetup,
    OvertimeEntries,
)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class SavingSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingScheme
        fields = "__all__"


class SavingSchemeEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingSchemeEntries
        fields = "__all__"


class TransactionEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionEntries
        fields = "__all__"


class PayrollFormularSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollFormular
        fields = "__all__"


class OvertimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeSetup
        fields = "__all__"


class OvertimeEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeEntries
        fields = "__all__"


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"


class LoanEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanEntries
        fields = "__all__"


class AuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditTrail
        fields = "__all__"


class EmployeeSavingSchemeEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSavingSchemeEntries
        fields = "__all__"


class EmployeeTransactionEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTransactionEntries
        fields = "__all__"


class ShiftSetUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftSetUp
        fields = "__all__"


class ShiftEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftEntries
        fields = "__all__"


class EmployeeShiftEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeShiftEntries
        fields = "__all__"

class PaymasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymaster
        fields = "__all__"
