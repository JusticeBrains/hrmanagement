import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from options.text_options import PaymentFrequency, AllowanceType, DeductionFrequency


class Transactions(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=50, blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=150, blank=True, null=True
    )
    start_period = models.ForeignKey(
        "calenders.Period", verbose_name=_("Start Period"), on_delete=models.CASCADE
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
        default=AllowanceType.ALLOWANCE,
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
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee ID"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Transactions"
        verbose_name_plural = "Transactions"

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
        "calenders.Period", verbose_name=_("Start Period"), on_delete=models.CASCADE
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
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee ID"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Saving Scheme"
        verbose_name_plural = "Saving Schemes"

    def __str__(self) -> str:
        return f"{self.code}"

    def __repr__(self):
        return f"{self.code}"
