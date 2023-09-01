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
    TaxLawType,
    TaxLaws,
    Transactions,
    SavingScheme,
    SavingSchemeEntries,
    TransactionEntries,
    PayrollFormular,
    OvertimeSetup,
    OvertimeEntries,
)


class TransactionSerializer(serializers.ModelSerializer):
    start_period = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    class Meta:
        model = Transactions
        fields = "__all__"


class SavingSchemeSerializer(serializers.ModelSerializer):
    start_period = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    class Meta:
        model = SavingScheme
        fields = "__all__"


class SavingSchemeEntriesSerializer(serializers.ModelSerializer):
    saving_scheme_name = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    employee_name = serializers.ReadOnlyField()
    start_period_code = serializers.ReadOnlyField()
    end_period_code = serializers.ReadOnlyField()
    percentage_of_employee_basic = serializers.ReadOnlyField()
    percentage_of_employer_basic = serializers.ReadOnlyField()
    class Meta:
        model = SavingSchemeEntries
        fields = "__all__"


class TransactionEntriesSerializer(serializers.ModelSerializer):
    transaction_name = serializers.ReadOnlyField()
    transaction_type = serializers.ReadOnlyField()
    company_name = serializers.ReadOnlyField()
    employee_name = serializers.ReadOnlyField()
    start_period_code = serializers.ReadOnlyField()
    end_period_code = serializers.ReadOnlyField()
    class Meta:
        model = TransactionEntries
        fields = "__all__"


class PayrollFormularSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollFormular
        fields = "__all__"


class OvertimeSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()
    class Meta:
        model = OvertimeSetup
        fields = "__all__"


class OvertimeEntriesSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()
    employee_name = serializers.ReadOnlyField()
    employee_code = serializers.ReadOnlyField()
    paygroup_no = serializers.ReadOnlyField()
    period_code = serializers.ReadOnlyField()
    year = serializers.ReadOnlyField()
    overtime_amount = serializers.ReadOnlyField()
    class Meta:
        model = OvertimeEntries
        fields = "__all__"


class LoansSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()
    period_code = serializers.ReadOnlyField()

    class Meta:
        model = Loans
        fields = "__all__"


class LoanEntriesSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()
    transaction_period_code = serializers.ReadOnlyField()
    deduction_start_period_code = serializers.ReadOnlyField()
    loan_name = serializers.ReadOnlyField()
    employee_name = serializers.ReadOnlyField()
    employee_code = serializers.ReadOnlyField()
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
    company_name = serializers.ReadOnlyField()
    period_code = serializers.ReadOnlyField()
    shift_name = serializers.ReadOnlyField()
    recurrent = serializers.ReadOnlyField()
    percentage_of_hourly_rate = serializers.ReadOnlyField()
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

class TaxLawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxLaws
        fields ="__all__"

class TaxLawTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxLawType
        fields ="__all__"
