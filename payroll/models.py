import json
import uuid
import math

from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from calenders.models import GlobalInputs
from options.text_options import (
    DisbursementType,
    InterestBasic,
    InterestCalculationType,
    PaymentFrequency,
    AllowanceType,
    DeductionFrequency,
    RecordType,
    TaxLawChoices,
    TaxType,
    TransactionType,
    WorkType,
)


class Transactions(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Start Period"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    start_period_code = models.CharField(
        _("Start Period Code"), max_length=50, blank=True, null=True
    )
    transaction_type = models.CharField(
        _("Transaction Type"),
        choices=TransactionType.choices,
        max_length=50,
        default=TransactionType.ALLOWANCE,
    )
    payment_frequency = models.CharField(
        _("Payment Frequency"),
        max_length=150,
        choices=PaymentFrequency.choices,
        default=PaymentFrequency.MONTHLY,
    )
    allowance_type = models.CharField(
        _("Allowance Type"),
        max_length=50,
        choices=AllowanceType.choices,
        null=True,
        blank=True,
    )
    interval = models.PositiveIntegerField(_("Interval"), default=1)
    prorate_new_staff = models.BooleanField(_("Prorate New Staff"), default=False)
    prorate_existing_staff = models.BooleanField(
        _("Prorate Existing Staff"), default=False
    )
    taxable = models.BooleanField(_("Taxable"), default=True)
    contribute_to_ssf = models.BooleanField(_("Contribute To SSF"), default=False)
    monthly_amount = models.DecimalField(
        _("Monthly Amount"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_basic = models.DecimalField(
        _("Percentage Of Basic"), max_digits=4, decimal_places=2, default=0.0
    )
    percentage_of_emolument = models.DecimalField(
        _("Percentage Of Emolument"), max_digits=4, decimal_places=2, default=0.0
    )
    ceiling = models.DecimalField(
        _("Ceiling"), max_digits=5, decimal_places=2, default=0.0
    )
    varying_amount = models.BooleanField(_("Varying Amount"), default=True)
    account_code = models.CharField(
        _("Account Code"), max_length=50, null=True, blank=True
    )
    currency = models.CharField(_("Currenct"), max_length=50, blank=True, null=True)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    recurring = models.BooleanField(_("Recurring"), default=False)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Transactions"
        verbose_name_plural = "Transactions"

    def populates_period_code(self):
        if self.start_period:
            self.start_period_code = self.start_period.period_code
        if self.company:
            self.company_name = self.company.name

    def save(self, *args, **kwargs):
        self.populates_period_code()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.description}"

    def __repr__(self):
        return f"{self.description}"


class SavingScheme(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Start Period"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    start_period_code = models.CharField(
        _("Start Period Code"), max_length=50, blank=True, null=True
    )
    deduction_frequency = models.CharField(
        _("Deduction Frequency"),
        max_length=150,
        choices=DeductionFrequency.choices,
        default=DeductionFrequency.MONTHLY,
    )
    prorate_new_staff = models.BooleanField(_("Prorate New Staff"), default=False)
    prorate_existing_staff = models.BooleanField(
        _("Prorate Existing Staff"), default=False
    )
    percentage_of_employee_basic = models.DecimalField(
        _("Percentage Of Employee Contribution"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
    percentage_of_employer_basic = models.DecimalField(
        _("Percentage Of Employer Basic"), max_digits=4, decimal_places=2, default=0.0
    )
    percentage_of_employee_gross = models.DecimalField(
        _("Percentage Of Employee Gross"), max_digits=4, decimal_places=2, default=0.0
    )
    percentage_of_employer_gross = models.DecimalField(
        _("Percentage Of Employer Gross"), max_digits=4, decimal_places=2, default=0.0
    )
    statutory = models.BooleanField(_("Statutory"), default=False)
    varying_amount = models.BooleanField(_("Varying Amount"), default=True)
    employee_tax_deductible = models.BooleanField(
        _("Employee Tax Deductible"), default=False
    )
    employer_taxable = models.BooleanField(_("Employer Taxable"), default=False)
    old_employee_contribution = models.DecimalField(
        _("Old Employee Contribution"), max_digits=8, decimal_places=2, default=0.0
    )
    old_employer_contribution = models.DecimalField(
        _("Old Employer Contribution"), max_digits=8, decimal_places=2, default=0.0
    )
    old_percentage_of_employer_basic = models.DecimalField(
        _("Old Percentage Of Employer Basic"),
        max_digits=4,
        decimal_places=2,
        default=0.0,
    )
    old_percentage_of_employee_basic = models.DecimalField(
        _("Old Percentage Of Employee Basic"),
        max_digits=4,
        decimal_places=2,
        default=0.0,
    )
    recurring = models.BooleanField(_("Recurring"), default=False)
    base = models.DecimalField(_("Base"), max_digits=10, decimal_places=2, default=0.0)
    ssnit_percentage = models.DecimalField(
        _("SSNIT Percentage"), max_digits=3, decimal_places=2, default=0.0
    )
    tier_2 = models.DecimalField(
        _("Tier 2"), max_digits=10, decimal_places=2, default=0.0
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Saving Scheme"
        verbose_name_plural = "Saving Schemes"

    def __str__(self) -> str:
        return f"{self.description}"

    def __repr__(self):
        return f"{self.description}"

    def populate_fields(self):
        if self.company:
            self.company_name = self.company.name
        if self.start_period:
            self.start_period_code = self.start_period.period_code

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class TransactionEntries(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    disbursement_type = models.CharField(
        _("Disbursement Type"),
        choices=DisbursementType.choices,
        max_length=50,
        blank=True,
        null=True,
    )
    transaction_code = models.ForeignKey(
        "payroll.Transactions",
        verbose_name=_("Transaction Code"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="trans_code",
    )
    transaction_type = models.CharField(
        _("Transaction Type"),
        choices=TransactionType.choices,
        max_length=50,
        null=True,
        blank=True,
    )
    transaction_name = models.CharField(
        _("Transaction Name"), max_length=50, blank=True, null=True
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee ID"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    recurrent = models.BooleanField(_("Recurrent"), default=False)
    start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Start Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="start_per_entries",
    )
    start_period_code = models.CharField(
        _("Start Period Code"), max_length=50, blank=True, null=True
    )
    end_period_code = models.CharField(
        _("End Period Code"), max_length=50, blank=True, null=True
    )
    end_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("End Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="end_per_entries",
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    percentage_of_basic = models.DecimalField(
        _("Percentage Of Basic"), max_digits=4, decimal_places=2, null=True, blank=True
    )
    taxable = models.BooleanField(_("Taxable"), default=False)
    contribute_to_ssf = models.BooleanField(_("Contribute To SSF"), default=False)
    global_id = models.CharField(_("Global ID"), max_length=250, blank=True, null=True)
    global_name = models.CharField(
        _("Global Name"), max_length=250, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    status = models.BooleanField(_("Status"), default=False)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Transaction Entries"
        verbose_name_plural = "Transaction Entries"

    def populate_fields(self):
        if self.transaction_code:
            self.transaction_name = self.transaction_code.description
            self.transaction_type = self.transaction_code.transaction_type
        if self.company:
            self.company_name = self.company.name
        if self.employee:
            self.employee_name = (
                f"{self.employee.last_name}, {self.employee.first_name}"
            )
        if self.start_period:
            self.start_period_code = self.start_period.period_code
        if self.end_period:
            self.end_period_code = self.end_period.period_code

    def __str__(self) -> str:
        return f"{self.disbursement_type}"

    def __repr__(self):
        return f"{self.disbursement_type}"

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class EmployeeTransactionEntries(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    employee = models.ForeignKey(
        "employee.Employee",
        on_delete=models.CASCADE,
        related_name="employee_transaction",
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=150, blank=True, null=True
    )
    transaction_entry = models.ForeignKey(
        "payroll.TransactionEntries",
        verbose_name=_("Transaction Name"),
        on_delete=models.CASCADE,
        related_name="employee_transaction",
    )
    transaction_entry_name = models.CharField(
        _("Transaction Name"), max_length=150, blank=True, null=True
    )
    transaction_type = models.CharField(
        _("Transaction Type"),
        choices=TransactionType.choices,
        max_length=50,
        null=True,
        blank=True,
    )
    recurrent = models.BooleanField(_("Recurrent"), default=True)
    start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Start Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="emp_start_per_entries",
    )
    start_period_code = models.CharField(
        _("Start Period Code"), max_length=50, blank=True, null=True
    )
    end_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("End Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="emp_per_entries",
    )
    end_period_code = models.CharField(
        _("End Period Code"), max_length=50, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_basic = models.DecimalField(
        _("Percentage Of Basic"), max_digits=4, decimal_places=2, null=True, blank=True
    )
    taxable = models.BooleanField(_("Taxable"), default=False)
    contribute_to_ssf = models.BooleanField(_("Contribute To SSF"), default=False)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    status = models.BooleanField(_("Status"), default=False)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Employee Transaction Entries"
        verbose_name_plural = "Employee Transaction Entries"

    def __str__(self) -> str:
        return f"{self.employee_name} {self.transaction_entry_name}"

    def __repr__(self):
        return f"{self.employee_name} {self.transaction_entry_name}"


class SavingSchemeEntries(models.Model):
    """
    Represents entries for a saving scheme.

    Fields:
    - id: Unique identifier for the saving scheme entry.
    - disbursement_type: Type of disbursement for the saving scheme entry.
    - employee: Foreign key to the related employee.
    - employee_name: Name of the employee.
    - savingscheme_code: Foreign key to the related saving scheme.
    - saving_scheme_name: Name of the saving scheme.
    - recurrent: Boolean field indicating if the saving scheme entry is recurrent.
    - start_period: Foreign key to the related start period.
    - start_period_code: Code for the start period.
    - end_period_code: Code for the end period.
    - end_period: Foreign key to the related end period.
    - employee_contribution: Amount of employee contribution for the saving scheme.
    - employer_contribution: Amount of employer contribution for the saving scheme.
    - percentage_of_employee_basic: Percentage of employee's basic salary for the saving scheme.
    - percentage_of_employer_basic: Percentage of employer's basic salary for the saving scheme.
    """

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    disbursement_type = models.CharField(
        _("Disbursement Type"), choices=DisbursementType.choices, blank=True, null=True
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    savingscheme_code = models.ForeignKey(
        "payroll.SavingScheme",
        verbose_name=_("Saving Scheme Code"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    saving_scheme_name = models.CharField(
        _("Saving Scheme Name"), max_length=150, blank=True, null=True
    )
    recurrent = models.BooleanField(_("Recurrent"), default=True)
    start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Start Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="saving_start_period",
    )
    start_period_code = models.CharField(
        _("Start Period Code"), max_length=50, blank=True, null=True
    )
    end_period_code = models.CharField(
        _("End Period Code"), max_length=50, blank=True, null=True
    )
    end_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("End Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="saving_end_per_entries",
    )
    percentage_of_employee_basic = models.DecimalField(
        _("Percentage Of Employee Basic"), max_digits=4, decimal_places=2, default=0.0
    )
    percentage_of_employer_basic = models.DecimalField(
        _("Percentage Of Employer Basic"), max_digits=4, decimal_places=2, default=0.0
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    global_id = models.CharField(_("Global ID"), max_length=250, blank=True, null=True)
    global_name = models.CharField(
        _("Global Name"), max_length=250, blank=True, null=True
    )
    status = models.BooleanField(_("Status"), default=False)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Saving Scheme Entries"
        verbose_name_plural = "Saving Scheme Entries"

    def __str__(self) -> str:
        return f"{self.savingscheme_code}"

    def __repr__(self) -> str:
        return f"{self.savingscheme_code}"

    def populate_fields(self):
        if self.savingscheme_code:
            self.saving_scheme_name = self.savingscheme_code.description
        if self.employee:
            self.employee_name = (
                f"{self.employee.last_name}, {self.employee.first_name}"
            )
        if self.company:
            self.company_name = self.company.name

        if self.start_period:
            self.start_period_code = self.start_period.period_code
        if self.end_period:
            self.end_period_code = self.end_period.period_code
        self.percentage_of_employee_basic = (
            self.savingscheme_code.percentage_of_employee_basic
            if self.savingscheme_code is not None
            else None
        )
        self.percentage_of_employer_basic = (
            self.savingscheme_code.percentage_of_employer_basic
            if self.savingscheme_code is not None
            else None
        )

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class EmployeeSavingSchemeEntries(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    employee = models.ForeignKey(
        "employee.Employee",
        on_delete=models.CASCADE,
        related_name="employee_saving_scheme",
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=150, blank=True, null=True
    )
    saving_scheme = models.ForeignKey(
        "payroll.SavingSchemeEntries",
        verbose_name=_("Saving Scheme"),
        on_delete=models.CASCADE,
        related_name="employee_entry",
    )
    saving_scheme_name = models.CharField(
        _("Saving Scheme Name"), max_length=150, blank=True, null=True
    )
    recurrent = models.BooleanField(_("Recurrent"), default=True)
    start_period_code = models.CharField(
        _("Start Period Code"), max_length=50, blank=True, null=True
    )
    end_period_code = models.CharField(
        _("End Period Code"), max_length=50, blank=True, null=True
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    employee_contribution = models.DecimalField(
        _("Employee Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    employer_contribution = models.DecimalField(
        _("Employer Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    status = models.BooleanField(_("Status"), default=False)
    # created_at = models.DateField(_("Created At"), auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Employee Saving Scheme Entries"
        verbose_name_plural = "Employee Saving Scheme Entries"

    def __str__(self) -> str:
        return f"{self.employee_name} {self.saving_scheme_name}"

    def __repr__(self):
        return f"{self.employee_name} {self.saving_scheme_name}"


class PayrollFormular(models.Model):
    """
    Represents a model for a payroll formula in a Django application.

    Fields:
    - id: Unique identifier for the payroll formula.
    - description: Description of the payroll formula.
    - shortname: Short name of the payroll formula.
    - inactive: Boolean field indicating whether the payroll formula is inactive.
    - hourly_rate: Hourly rate for the payroll formula.
    - overtime_hours: Overtime hours for the payroll formula.
    - company: Foreign key to the Company model representing the company associated with the payroll formula.
    - company_name: Name of the company associated with the payroll formula.
    - user_id: Foreign key to the CustomUser model representing the user associated with the payroll formula.
    - updated_at: Date and time when the payroll formula was last updated.
    - created_at: Date and time when the payroll formula was created.

    Methods:
    - __str__(): Returns a string representation of the payroll formula in the format "{shortname} - {hourly_rate}".
    - __repr__(): Returns a string representation of the payroll formula in the format "{shortname} - {hourly_rate}".
    - populate_fields(): Populates the company name field based on the related company model.
    - save(): Overrides the default save method to automatically populate fields and save the payroll formula.
    """

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    shortname = models.CharField(_("Short Name"), max_length=150, blank=True, null=True)
    inactive = models.BooleanField(_("Inactive"), default=True)
    hourly_rate = models.DecimalField(
        _("Hourly Rate"), max_digits=5, decimal_places=2, default=0.0
    )
    overtime_hours = models.DecimalField(
        _("Overtime Hours"), max_digits=5, decimal_places=2, default=0.0
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    created_at = models.DateField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = "Payroll Formular"
        verbose_name_plural = "Payroll Formular"

    def __str__(self):
        """
        Returns a string representation of the payroll formula in the format "{shortname} - {hourly_rate}".
        """
        return f"{self.shortname} - {self.hourly_rate}"

    def __repr__(self):
        """
        Returns a string representation of the payroll formula in the format "{shortname} - {hourly_rate}".
        """
        return f"{self.shortname} - {self.hourly_rate}"

    def populate_fields(self):
        """
        Populates the company name field based on the related company model.
        """
        if self.company:
            self.company_name = self.company.name

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically populate fields and save the payroll formula.
        """
        self.populate_fields()
        super().save(*args, **kwargs)


class OvertimeSetup(models.Model):
    """
    Represents the setup for overtime work.

    Fields:
    - id: Unique identifier for the overtime setup.
    - description: Description of the overtime setup.
    - payroll_formular: Foreign key to the PayrollFormular model representing the payroll formula associated with the overtime setup.
    - company: Foreign key to the Company model representing the company associated with the overtime setup.
    - company_name: Name of the company associated with the overtime setup.
    - user_id: Foreign key to the CustomUser model representing the user associated with the overtime setup.
    - created_at: Date and time when the overtime setup was created.
    - updated_at: Date and time when the overtime setup was last updated.
    """

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    payrollformular = models.ForeignKey(
        "PayrollFormular", on_delete=models.DO_NOTHING, related_name="overtimes"
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Overtime Setup"
        verbose_name_plural = "Overtime Setups"

    def __str__(self):
        """
        Returns a string representation of the overtime setup.

        Returns:
        - A string in the format "{id} : {description}".
        """
        return f"{self.id} : {self.description or ''}"

    def populate_fields(self):
        """
        Populates the company name field based on the related company model.
        """
        if self.company:
            self.company_name = self.company.name

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically populate fields and save the overtime setup.
        """
        self.populate_fields()
        super().save(*args, **kwargs)


class OvertimeEntries(models.Model):
    """
    The `OvertimeEntries` class is a Django model that represents entries for overtime work. It stores information about the employee, overtime setup, company, date, hours worked, and the calculated overtime amount.

    Example Usage:
        # Create a new overtime entry
        entry = OvertimeEntries()
        entry.employee = employee
        entry.overtime = overtime_setup
        entry.company = company
        entry.date = date
        entry.no_of_hours = hours_worked
        entry.save()

        # Retrieve all overtime entries for a specific employee
        entries = OvertimeEntries.objects.filter(employee=employee)

        # Calculate the total overtime amount for a specific period
        total_amount = OvertimeEntries.objects.filter(period=period).aggregate(Sum('overtime_amount'))

    Main functionalities:
    - Store information about overtime work entries, including the employee, overtime setup, company, date, hours worked, and calculated overtime amount.
    - Automatically populate fields such as employee name, employee code, paygroup number, company name, period code, and year based on related models and input data.
    - Calculate the overtime amount based on the employee's annual basic salary, total working hours, and number of overtime hours worked.

    Methods:
    - `populate_fields()`: Populates fields such as employee name, employee code, paygroup number, company name, period code, and year based on related models and input data.
    - `save()`: Overrides the default save method to automatically populate fields and save the overtime entry.

    Fields:
    - `id`: Unique identifier for the overtime entry.
    - `employee`: Foreign key to the Employee model representing the employee associated with the overtime entry.
    - `employee_code`: Code of the employee associated with the overtime entry.
    - `employee_name`: Name of the employee associated with the overtime entry.
    - `paygroup_no`: Paygroup number of the employee associated with the overtime entry.
    - `overtime`: Foreign key to the OvertimeSetup model representing the overtime setup associated with the overtime entry.
    - `overtime_name`: Name of the overtime setup associated with the overtime entry.
    - `company`: Foreign key to the Company model representing the company associated with the overtime entry.
    - `company_name`: Name of the company associated with the overtime entry.
    - `date`: Start date of the overtime work.
    - `status`: Boolean field indicating the status of the overtime entry.
    - `user_id`: Foreign key to the CustomUser model representing the user associated with the overtime entry.
    - `period`: Foreign key to the Period model representing the period associated with the overtime entry.
    - `period_code`: Code of the period associated with the overtime entry.
    - `no_of_hours`: Number of overtime hours worked.
    - `overtime_amount`: Calculated overtime amount based on the employee's annual basic salary, total working hours, and number of overtime hours worked.
    - `year`: Year of the period associated with the overtime entry.
    - `created_at`: Date and time when the overtime entry was created.
    - `updated_at`: Date and time when the overtime entry was last updated."""

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=150, blank=True, null=True
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    paygroup_no = models.CharField(
        _("PayGroup No"), max_length=50, blank=True, null=True
    )
    overtime = models.ForeignKey(
        "payroll.OvertimeSetup",
        verbose_name=_("Overtime"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    overtime_name = models.CharField(
        _("Ovetime Name"), max_length=150, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    date = models.DateField(_("Start Date"), auto_now=True)
    status = models.BooleanField(_("Status"), default=False)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    period_code = models.CharField(
        _("Period Code"), max_length=50, blank=True, null=True
    )
    no_of_hours = models.DecimalField(
        _("No Of Hours"), max_digits=5, decimal_places=2, default=0.0
    )
    overtime_amount = models.DecimalField(
        _("Overtime Amount"), max_digits=8, decimal_places=2, default=0.0
    )
    year = models.PositiveIntegerField(_("Year"), blank=True, null=True)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Ovetime Entries"
        verbose_name_plural = "Ovetime Entries"

    def __str__(self):
        return f"{self.employee_code} {self.date}"

    def __repr__(self):
        return f"{self.employee_code} {self.date}"

    def populate_fields(self):
        if self.employee:
            self.employee_name = f"{self.employee.first_name} {self.employee.last_name}"
            self.employee_code = self.employee.code
            self.paygroup_no = self.employee.pay_group_name
        if self.company:
            self.company_name = self.company.name
        if self.period:
            self.period_code = self.period.period_code
            self.year = self.period.period_year.year
        if self.overtime and self.employee.annual_basic is not None:
            annual_basic = Decimal(self.employee.annual_basic)
            amount = annual_basic * 12
            total_working_hours = GlobalInputs.objects.get(company=self.company)
            if total_working_hours:
                self.overtime_amount = float(
                    (amount / total_working_hours.annual_working_hours)
                    * self.no_of_hours
                )
        elif self.overtime:
            self.overtime_name = self.overtime.description

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class Loans(models.Model):
    """
    Represents a model for loans in a payroll system.

    Fields:
    - id: Unique identifier for the loan object
    - name: Name of the loan
    - min_loan_amount: Minimum loan amount allowed
    - max_loan_amount: Maximum loan amount allowed
    - max_loan_term: Maximum loan term in months
    - max_percentage_of_basic: Maximum percentage of basic salary that can be borrowed
    - interest_rate: Interest rate for the loan
    - interest_calculation_type: Type of interest calculation (e.g., Flat Rate, Amortization)
    - interest_basic: Basic unit for interest calculation (e.g., Per Month, Per Annum)
    - grace_periods: Number of grace periods before loan repayment starts
    - percentage: Percentage of loan amount to be deducted from salary
    - user_id: Foreign key to the associated user object
    - company: Foreign key to the associated company object
    - company_name: Name of the associated company
    - created_at: Date and time of loan creation
    - period: Foreign key to the associated period object
    - period_code: Code of the associated period
    - updated_at: Date and time of loan update

    Methods:
    - __str__(): Returns a string representation of the loan object
    - __repr__(): Returns a string representation of the loan object
    - populate_fields(): Populates the company_name and period_code fields based on the associated company and period objects, respectively
    - save(): Overrides the default save() method to automatically populate the fields and save the loan object
    """

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)
    min_loan_amount = models.DecimalField(
        _("Minimum Amount"), max_digits=8, decimal_places=2, default=0.0
    )
    max_loan_amount = models.DecimalField(
        _("Maximum Amount"), max_digits=10, decimal_places=2, default=0.0
    )
    max_loan_term = models.PositiveIntegerField(_("Max Loan Term"), default=0)
    max_percentage_of_basic = models.DecimalField(
        _("Max Percentage Of Basic"), max_digits=5, decimal_places=2, default=0.0
    )
    interest_rate = models.DecimalField(
        _("Interest Rate"), max_digits=5, decimal_places=2, default=0.0
    )
    interest_calculation_type = models.CharField(
        _("Interest Calculation Type"),
        choices=InterestCalculationType.choices,
        max_length=50,
    )
    interest_basic = models.CharField(
        _("Interest Basic"), choices=InterestBasic.choices, max_length=50
    )
    grace_periods = models.PositiveIntegerField(_("Grace Periods"), default=0)
    percentage = models.DecimalField(
        _("Percentage"), max_digits=5, decimal_places=2, default=0.0
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    period_code = models.CharField(
        _("Period Code"), max_length=50, blank=True, null=True
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Loans"
        verbose_name_plural = "Loans"

    def __str__(self) -> str:
        """
        Returns a string representation of the loan object.

        Returns:
        - str: The name of the loan
        """
        return f"{self.name}"

    def __repr__(self):
        """
        Returns a string representation of the loan object.

        Returns:
        - str: The name of the loan
        """
        return f"{self.name}"

    def populate_fields(self):
        """
        Populates the company_name and period_code fields based on the associated company and period objects, respectively.
        """
        if self.company:
            self.company_name = self.company.name
        if self.period:
            self.period_code = self.period.period_code

    def save(self, *args, **kwargs):
        """
        Overrides the default save() method to automatically populate the fields and save the loan object.
        """
        self.populate_fields()
        super().save(*args, **kwargs)


class LoanEntries(models.Model):
    """
    Represents entries for loans.

    Fields:
    - id: Unique identifier for the loan entry
    - loan: Foreign key to the associated loan object
    - loan_name: Name of the loan
    - description: Description of the loan
    - amount: Amount of the loan
    - employee: Foreign key to the associated employee object
    - employee_code: Code of the employee
    - employee_name: Name of the employee
    - interest_rate: Interest rate of the loan
    - periodic_principal: Principal amount to be repaid periodically
    - no_of_repayments: Number of repayments for the loan
    - transaction_period: Foreign key to the associated transaction period object
    - transaction_period_code: Code of the transaction period
    - deduction_start_period: Foreign key to the associated deduction start period object
    - deduction_start_period_code: Code of the deduction start period
    """

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    loan = models.ForeignKey(
        "payroll.Loans",
        verbose_name=_("Loan ID"),
        related_name="loanentries",
        on_delete=models.DO_NOTHING,
    )
    loan_name = models.CharField(_("Loan Name"), max_length=150, blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=10, decimal_places=4, default=0.0
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=150, blank=True, null=True
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    interest_rate = models.DecimalField(
        _("Interest Rate"),
        max_digits=5,
        decimal_places=2,
        default=0.0,
        blank=True,
        null=True,
    )
    periodic_principal = models.DecimalField(
        _("Periodic Principal"), max_digits=8, decimal_places=2, default=0.0
    )
    monthly_repayment = models.DecimalField(
        _("Monthly Repayment"), max_digits=10, decimal_places=4, blank=True, null=True
    )
    total_amount_paid = models.DecimalField(
        _("Total Amount Paid"), max_digits=10, decimal_places=4, blank=True, null=True
    )
    duration = models.DecimalField(
        _("Duration"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    transaction_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Transaction Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    transaction_period_code = models.CharField(
        _("Transaction Period Code"), max_length=50, blank=True, null=True
    )
    deduction_start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="loan_entries_deduction",
    )
    deduction_start_period_code = models.CharField(
        _("Deduction Start Period Code"), max_length=50, blank=True, null=True
    )
    deduction_end_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Deduction End Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="end_entries_deduction",
    )
    deduction_end_period_code = models.CharField(
        _("Deduction End Period Code"), max_length=50, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    schedule = models.JSONField(
        _("Schedule"),
        encoder=json.JSONEncoder,
        decoder=json.JSONDecoder,
        null=True,
        blank=True,
    )
    status = models.BooleanField(_("Status"), default=False)
    closed = models.BooleanField(_("Closed"), default=False)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = "Loan Entries"
        verbose_name_plural = "Loan Entries"

    def __str__(self) -> str:
        return f"{self.loan_name}"

    def __repr__(self):
        return f"{self.loan_name}"

    def populate_fields(self):
        self.company_name = self.company.name if self.company else None
        self.transaction_period_code = (
            self.transaction_period.period_code if self.transaction_period else None
        )
        self.deduction_start_period_code = (
            self.deduction_start_period.period_code
            if self.deduction_start_period
            else None
        )
        self.loan_name = self.loan.name if self.loan else None
        if self.employee:
            self.employee_name = f"{self.employee.first_name} {self.employee.last_name}"
            self.employee_code = self.employee.code

        if self.amount and self.monthly_repayment:
            # if self.duration is None:
            self.duration = self.amount / self.monthly_repayment
            # elif self.duration is not None:
            #     self.duration = self.duration

        if self.amount and self.duration:
            # if self.monthly_repayment is None:
            self.monthly_repayment = self.amount / self.duration
            # elif self.monthly_repayment is not None:
            #     self.monthly_repayment = self.monthly_repayment

        if self.total_amount_paid is not None:
            if self.total_amount_paid == self.amount:
                self.closed = True
                self.status = False

        if self.amount and self.duration and self.monthly_repayment:
            schedule = []
            amount_left = self.amount
            for month in range(1, math.ceil(self.duration) + 1):
                monthly_payment = min(self.monthly_repayment, amount_left)
                amount_left = round(amount_left - monthly_payment, ndigits=4)
                schedule.append(
                    {
                        "month": month,
                        "monthly_payment": float(monthly_payment),
                        "balance": float(amount_left),
                    }
                )
            self.schedule = schedule

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class EmployeeLoanPayment(models.Model):
    """
    Represents entries for loans.

    Fields:
    - id: Unique identifier for the loan entry
    - loan: Foreign key to the associated loan object
    - loan_name: Name of the loan
    - description: Description of the loan
    - amount: Amount of the loan
    - employee: Foreign key to the associated employee object
    - employee_code: Code of the employee
    - employee_name: Name of the employee
    - interest_rate: Interest rate of the loan
    - periodic_principal: Principal amount to be repaid periodically
    - no_of_repayments: Number of repayments for the loan
    - transaction_period: Foreign key to the associated transaction period object
    - transaction_period_code: Code of the transaction period
    - deduction_start_period: Foreign key to the associated deduction start period object
    - deduction_start_period_code: Code of the deduction start period
    """

    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    loan = models.ForeignKey(
        "payroll.Loans",
        verbose_name=_("Loan ID"),
        related_name="loan_payment_entries",
        on_delete=models.DO_NOTHING,
    )
    loan_name = models.CharField(_("Loan Name"), max_length=150, blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=10, decimal_places=4, default=0.0
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=150, blank=True, null=True
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    periodic_principal = models.DecimalField(
        _("Periodic Principal"), max_digits=8, decimal_places=2, default=0.0
    )
    monthly_repayment = models.DecimalField(
        _("Monthly Repayment"), max_digits=10, decimal_places=4, blank=True, null=True
    )
    total_amount_paid = models.DecimalField(
        _("Total Amount Paid"), max_digits=10, decimal_places=4, default=0.0
    )
    duration = models.DecimalField(
        _("Duration"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    transaction_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Transaction Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    transaction_period_code = models.CharField(
        _("Transaction Period Code"), max_length=50, blank=True, null=True
    )
    deduction_start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="loan_payment",
    )
    deduction_start_period_code = models.CharField(
        _("Deduction Start Period Code"), max_length=50, blank=True, null=True
    )
    deduction_end_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Deduction End Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="end_payment",
    )
    deduction_end_period_code = models.CharField(
        _("Deduction End Period Code"), max_length=50, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    paid = models.BooleanField(_("Paid"), default=False)

    class Meta:
        verbose_name = "Employee Monthly Loan Payment"
        verbose_name_plural = "Employee Monthly Loan Payment"

    def __str__(self):
        return self.loan_name

    def __repr__(self):
        return self.loan_name


class AuditTrail(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    process_id = models.TextField(_("Process ID"), blank=True, null=True)
    ip_address = models.CharField(
        _("IP Address"), max_length=150, blank=True, null=True
    )
    browser = models.CharField(_("Browser"), max_length=150, blank=True, null=True)
    company = models.ForeignKey(
        "company.Company", verbose_name=_("Company"), on_delete=models.DO_NOTHING
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = "Audit Trail"
        verbose_name_plural = "Audit Trails"

    def populate_fields(self):
        """
        Populates the company_name field with the name of the associated company.
        """
        if self.company:
            self.company_name = self.company.name

    def save(self, *args, **kwargs):
        """
        Overrides the save method to call populate_fields before saving the audit trail entry.
        """
        self.populate_fields()
        super().save(*args, **kwargs)


class ShiftSetUp(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)
    flat_rate = models.DecimalField(
        _("Flat Rate"), max_digits=5, decimal_places=2, default=0.0
    )
    percentage_of_daily_wage = models.DecimalField(
        _("Percentage Of Daily Wage"), max_digits=5, decimal_places=2, default=0.0
    )
    percentage_of_hourly_rate = models.DecimalField(
        _("Percentage Of Hourly Rate"), max_digits=5, decimal_places=2, default=0.0
    )
    recurring = models.BooleanField(_("Recurring"), default=True)
    work_type = models.CharField(
        _("Work Type"), choices=WorkType.choices, max_length=50, blank=True, null=True
    )
    record_type = models.CharField(
        _("Record Type"),
        choices=RecordType.choices,
        max_length=50,
        blank=True,
        null=True,
    )
    taxable = models.BooleanField(_("Taxable"), default=True)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User Id"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    created_at = models.DateTimeField(
        _("Created At"), auto_now=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = "Shift SetUp"
        verbose_name_plural = "Shift SetUps"

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class ShiftEntries(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    disbursement_type = models.CharField(
        _("Disbursement Type"),
        choices=DisbursementType.choices,
        max_length=50,
        blank=True,
        null=True,
    )
    shift_code = models.ForeignKey(
        "payroll.ShiftSetUp",
        verbose_name=_("Shift Code"),
        on_delete=models.CASCADE,
    )
    shift_name = models.CharField(
        _("Shift Name"), max_length=150, blank=True, null=True
    )
    no_of_shift = models.PositiveIntegerField(_("No Of Shift"), default=0)
    no_of_hours = models.DecimalField(
        _("No Of Hours"), max_digits=9, decimal_places=2, default=0.0
    )
    percentage_of_hourly_rate = models.DecimalField(
        _("Percentage Of Hourly"), max_digits=9, decimal_places=2, default=0.0
    )
    shift_amount = models.DecimalField(
        _("Shift Amount"), max_digits=9, decimal_places=2, default=0.0
    )
    period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    status = models.BooleanField(_("Status"), default=False)
    recurrent = models.BooleanField(_("Reccurent"), default=False)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    global_id = models.CharField(_("Global ID"), max_length=250, blank=True, null=True)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(
        _("Created At"), auto_now=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = "Shift Entries"
        verbose_name_plural = "Shift Entries"

    def __str__(self) -> str:
        return f"{self.shift_code}"

    def __repr__(self):
        return f"{self.shift_code}"

    def populate_fields(self):
        """
        Populates the company_name and period_code fields based on the associated company and period objects, respectively.
        """
        if self.company:
            self.company_name = self.company.name
        if self.period:
            self.period_code = self.period.period_code
        if self.shift_code:
            self.shift_name = self.shift_code.name
            self.recurrent = self.shift_code.recurring
            self.percentage_of_hourly_rate = self.shift_code.percentage_of_hourly_rate

    def save(self, *args, **kwargs):
        """
        Overrides the save method to call populate_fields before saving the setup entries.
        """
        self.populate_fields()
        super().save(*args, **kwargs)


class EmployeeShiftEntries(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    shift_code = models.ForeignKey(
        "payroll.ShiftEntries",
        verbose_name=_("Shift Code"),
        on_delete=models.CASCADE,
    )
    shift_name = models.CharField(
        _("Shift Name"), max_length=150, blank=True, null=True
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=50, blank=True, null=True
    )
    period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User Id"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    status = models.BooleanField(_("Status"), default=False)
    recurrent = models.BooleanField(_("Recurrent"), default=False)
    no_of_shift = models.DecimalField(
        _("No Of Shift"), max_digits=9, decimal_places=2, default=0.0
    )
    no_of_hours = models.DecimalField(
        _("No Of Hours"), max_digits=9, decimal_places=2, default=0.0
    )
    percentage_of_hourly_rate = models.DecimalField(
        _("Percentage Of Hourly_rate"), max_digits=5, decimal_places=2, default=0.0
    )
    percentage_of_daily_wage = models.DecimalField(
        _("Percentage Of Daily Wage"), max_digits=5, decimal_places=2, default=0.0
    )
    shift_amount = models.DecimalField(
        _("Shift Amount"), max_digits=9, decimal_places=2, default=0.0
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField(
        _("Created At"), auto_now=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = "Employee Shift Entries"
        verbose_name_plural = "Employee Shift Entries"

    def __str__(self) -> str:
        return f"{self.shift_code}"

    def __repr__(self):
        return f"{self.shift_code}"

    def populate_fields(self):
        """
        Populates the company_name and period_code fields based on the associated company and period objects, respectively.
        """
        if self.company:
            self.company_name = self.company.name
        if self.period:
            self.period_code = self.period.period_code
        if self.shift_code:
            self.shift_name = self.shift_code.shift_name
            self.recurrent = self.shift_code.recurrent
            self.percentage_of_hourly_rate = self.shift_code.percentage_of_hourly_rate
        if self.employee:
            self.employee_name = f"{self.employee.first_name} {self.employee.last_name}"
            self.employee_code = self.employee.code

    def save(self, *args, **kwargs):
        """
        Overrides the save method to call populate_fields before saving the employee shift entry
        """
        self.populate_fields()
        super().save(*args, **kwargs)


class Paymaster(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        related_name="paymaster_company",
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        related_name="paymaster_employee",
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    employee_code = models.CharField(_("Employee Code"), max_length=50)
    basic_salary = models.DecimalField(
        _("Basic Salary"), max_digits=20, decimal_places=2, default=0.0
    )
    allowances = models.DecimalField(
        _("Allowances"), max_digits=20, decimal_places=2, default=0.0
    )
    deductions = models.DecimalField(
        _("Deductions"), max_digits=20, decimal_places=2, default=0.0
    )
    ssf_employee = models.DecimalField(
        _("SSF Employee"), max_digits=10, decimal_places=2, default=0.0
    )
    gross_salary = models.DecimalField(
        _("Gross Salary"), max_digits=10, decimal_places=2, default=0.0
    )
    net_salary = models.DecimalField(
        _("Net Salary"), max_digits=20, decimal_places=2, default=0.0
    )
    taxable_salary = models.DecimalField(
        _("Taxable Salary"), max_digits=5, decimal_places=2, default=0.0
    )
    saving_scheme = models.DecimalField(
        _("Saving Schemes"), max_digits=10, decimal_places=2, default=0.0
    )
    loans = models.DecimalField(
        _("Loans"), max_digits=10, decimal_places=2, default=0.0
    )
    total_deductions = models.DecimalField(
        _("Total Deductions"), max_digits=10, decimal_places=2, default=0.0
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Period"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    period_name = models.CharField(
        _("Period Name"), max_length=50, blank=True, null=True
    )
    payslip = models.JSONField(
        _("PaySlip"),
        encoder=json.JSONEncoder,
        decoder=json.JSONDecoder,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Paymaster"
        verbose_name_plural = "Paymaster"

    def __str__(self) -> str:
        return f"{self.company_name}"

    def __repr__(self):
        return f"{self.company_name}" if self.company_name is not None else None

    def populate_fields(self):
        self.company_name = self.company.name if self.company is not None else None
        self.employee_code = self.employee.code if self.employee is not None else None
        self.employee_name = (
            f"{self.employee.last_name} {self.employee.first_name} {self.employee.middle_name}"
            if self.employee is not None
            else None
        )
        self.period_name = self.period.period_name if self.period is not None else None

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class TaxLaws(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    no = models.CharField(_("No."), max_length=50, blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=50, blank=True, null=True
    )
    tax_type = models.CharField(
        _("Tax Type"), choices=TaxType.choices, max_length=150, blank=True, null=True
    )
    bonus_tax_rate = models.DecimalField(
        _("Bonus Tax rate"), max_digits=5, decimal_places=2, default=5.0
    )
    bonus_percentage_threshold = models.DecimalField(
        _("Bonus Percentage Threshold"), max_digits=5, decimal_places=2, default=0.0
    )
    annual_bonus_threshold = models.DecimalField(
        _("Annual Bonus Threshold"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    overtime_threshold = models.DecimalField(
        _("Overtime Threshold"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Tax Laws"
        verbose_name_plural = "Tax Laws"

    def __str__(self) -> str:
        return f"{self.no} {self.description}"

    def __repr__(self) -> str:
        return f"{self.no} {self.description}"


class TaxLawType(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    tax_law_type = models.CharField(
        _("Tax Law Type"),
        choices=TaxLawChoices.choices,
        max_length=150,
        blank=True,
        null=True,
    )
    tax_law = models.ForeignKey(
        "payroll.TaxLaws",
        verbose_name=_("Tax Law"),
        on_delete=models.CASCADE,
        related_name="tax_law_type",
    )
    tax_law_name = models.CharField(
        _("Tax Law Name"), max_length=150, blank=True, null=True
    )
    percentage = models.DecimalField(
        _("Percenatge"), max_digits=5, decimal_places=2, default=0.0
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=10, decimal_places=2, default=0.0
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Tax Law Type"
        verbose_name_plural = "Tax Law Types"

    def save(self, *args, **kwargs):
        self.tax_law_name = (
            self.tax_law.description if self.tax_law is not None else None
        )
        self.company_name = self.company.name if self.company is not None else None
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.tax_law_name}"

    def __repr__(self) -> str:
        return f"{self.tax_law_name}"


class TaxRelief(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=150, blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    benefit_relief = models.BooleanField(_("Benefit Relief"), default=False)
    maximum_no = models.PositiveIntegerField(_("Maximum No"), default=0)
    rate = models.DecimalField(_("Rate"), max_digits=5, decimal_places=2, default=0.0)
    maximum_age = models.PositiveIntegerField(_("Maximum Age"), default=0)
    minimum_age = models.PositiveIntegerField(_("Minimum Age"), default=0)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        related_name="tax_relief_company",
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Tax Relief"
        verbose_name_plural = "Tax Relief"

    def __str__(self) -> str:
        return f"{self.description}"

    def __repr__(self):
        return f"{self.description}"

    def save(self, *args, **kwargs):
        self.company_name = self.company.name if self.company is not None else None
        super().save(*args, **kwargs)
