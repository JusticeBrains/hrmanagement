from rest_framework import serializers

from .models import (
    LoanEntries,
    Loans,
    Transactions,
    SavingScheme,
    SavingSchemeEntries,
    TransactionEntries,
    PayrollFormular,
    OvertimeSetup,
    OvertimeEntries
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
