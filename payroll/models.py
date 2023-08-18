import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from options.text_options import (
    DisbursementType,
    PaymentFrequency,
    AllowanceType,
    DeductionFrequency,
    TransactionType,
)


class Transactions(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=50, blank=True, null=True)
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
        _("Percentage Of Basic"), max_digits=3, decimal_places=2, default=0.0
    )
    percentage_of_emolument = models.DecimalField(
        _("Percentage Of Emolument"), max_digits=3, decimal_places=2, default=0.0
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
        return f"{self.code}"

    def __repr__(self):
        return f"{self.code}"


class SavingScheme(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=50, blank=True, null=True)
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
    employee_contribution = models.DecimalField(
        _("Employee Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_employee_basic = models.DecimalField(
        _("Percentage Of Employee Contribution"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
    employer_contribution = models.DecimalField(
        _("Employer Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_employer_basic = models.DecimalField(
        _("Percentage Of Employer Basic"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_employee_gross = models.DecimalField(
        _("Percentage Of Employee Gross"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_employer_gross = models.DecimalField(
        _("Percentage Of Employer Gross"), max_digits=10, decimal_places=2, default=0.0
    )
    statutory = models.BooleanField(_("Statutory"), default=False)
    varying_amount = models.BooleanField(_("Varying Amount"), default=True)
    employee_tax_deductible = models.BooleanField(
        _("Employee Tax Deductible"), default=False
    )
    employer_taxable = models.BooleanField(_("Employer Taxable"), default=False)
    old_employee_contribution = models.DecimalField(
        _("Old Employee Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    old_employer_contribution = models.DecimalField(
        _("Old Employer Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    old_percentage_of_employer_basic = models.DecimalField(
        _("Old Percentage Of Employer Basic"),
        max_digits=3,
        decimal_places=2,
        default=0.0,
    )
    recurring = models.BooleanField(_("Recurring"), default=False)
    base = models.DecimalField(_("Base"), max_digits=10, decimal_places=2, default=0.0)
    ssnit_percentage = models.DecimalField(
        _("SSNIT Percentage"), max_digits=10, decimal_places=2, default=0.0
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

    class Meta:
        verbose_name = "Saving Scheme"
        verbose_name_plural = "Saving Schemes"

    def __str__(self) -> str:
        return f"{self.code}"

    def __repr__(self):
        return f"{self.code}"

    def populate_fields(self):
        if self.company:
            self.company_name = self.company.name
        if self.start_period:
            self.start_period_code = self.start_period.description

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
        null=True, blank=True
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
    department = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    department_name = models.CharField(
        _("Department Name"), max_length=150, blank=True, null=True
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
    type_code = models.CharField(_("Type Code"), max_length=50, blank=True, null=True)
    recurrenct = models.BooleanField(_("Recurrent"), default=False)
    start_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("Start Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="start_per_entries",
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
        _("Amount"), max_digits=8, decimal_places=2, default=0.0
    )
    percentage_of_basic = models.DecimalField(
        _("Percentage Of Basic"), max_digits=3, decimal_places=2, null=True, blank=True
    )
    taxable = models.BooleanField(_("Taxable"), default=False)
    contribute_to_ssf = models.BooleanField(_("Contribute To SSF"), default=False)

    class Meta:
        verbose_name = "Transaction Entries"
        verbose_name_plural = "Transaction Entries"

    def populate_fields(self):
        if self.transaction_code:
            self.transaction_name = self.transaction_code.description
        if self.company:
            self.company_name = self.company.name
        if self.department:
            self.department_name = self.department.name
        if self.employee:
            self.employee_name = (
                f"{self.employee.last_name}, {self.employee.first_name}"
            )

    def __str__(self) -> str:
        return f"{self.disbursement_type}"

    def __repr__(self):
        return f"{self.disbursement_type}"

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class SavingSchemeEntries(models.Model):
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
    end_period = models.ForeignKey(
        "calenders.Period",
        verbose_name=_("End Period"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="saving_end_period",
    )
    employee_contribution = models.DecimalField(
        _("Employee Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    employer_contribution = models.DecimalField(
        _("Employer Contribution"), max_digits=10, decimal_places=2, default=0.0
    )
    percentage_of_employee_basic = models.DecimalField(
        _("Percentage Of Employee Basic"), max_digits=3, decimal_places=2, default=0.0
    )
    percentage_of_employer_basic = models.DecimalField(
        _("Percentage Of Employer Basic"), max_digits=3, decimal_places=2, default=0.0
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

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

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)
