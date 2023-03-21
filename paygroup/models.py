from django.db import models
from django.utils.translation import gettext_lazy as _
from options import text_options


class PayGroup(models.Model):
    no = models.CharField(_("No."), max_length=50)
    description = models.TextField(_("Description"))
    short_name = models.CharField(_("Short Name"), max_length=50)
    overtime_code = models.ForeignKey("CalculationHeader", verbose_name=_("Overtime Code"), on_delete=models.CASCADE)
    overtime_description = models.TextField(_("Overtime Description"))
    limit_amount = models.DecimalField(_("Limit Amount"), max_digits=5, decimal_places=2)
    limit_percent = models.DecimalField(_("Limit Percent(Basic)"), max_digits=5, decimal_places=2)
    taxable_inocme_code = models.CharField(_("Taxable Income Code"), max_length=50)
    taxable_inocme_description = models.TextField(_("Taxable Income Description"))
    tax_code = models.ForeignKey("TaxLaws", verbose_name=_("Tax Code"), on_delete=models.CASCADE, related_name="tax_code")
    tax_description = models.CharField(_("Tax Description"), max_length=150)
    tax_relief_code = models.ForeignKey("TaxReliefs", verbose_name=_("Tax Reliefs"), on_delete=models.CASCADE)
    tax_relief_name = models.CharField(_("Tax Relief Name"), max_length=150)
    gross_income_code = models.CharField(_("CalculationHeader"), max_length=50)
    gross_income_description = models.CharField(_("Gross Income Description"), max_length=150)
    currency_code = models.ForeignKey("Currency", verbose_name=_("Currency Code"), on_delete=models.CASCADE)
    bonus_tax_code = models.ForeignKey("TaxLaws", verbose_name=_("Bonus Tax Code"), on_delete=models.CASCADE, related_name="bonus_tax_code")
    bonus_tax_description = models.CharField(_("Bonus Tax Description"), max_length=150)
    commission_percentage = models.DecimalField(_("Commission Percentage"), max_digits=5, decimal_places=2)
    tax_percentage_on_commission = models.DecimalField(_("Tax Percentage on Commission"), max_digits=5, decimal_places=2)
    gross_up = models.BooleanField(_("Gross Up"))

    class Meta:
        verbose_name = "Pay Group"
        verbose_name_plural = "Pay Groups"


class CalculationHeader(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    description = models.CharField(_("Description"), max_length=150)
    short_name = models.CharField(_("Short Name"), max_length=50)
    inactive = models.BooleanField(_("Inactive"))

    class Meta:
        verbose_name = "Calculation Header"
        verbose_name_plural = "Calculation Headers"


class TaxLaws(models.Model):
    no = models.CharField(_("No."), max_length=50)
    description = models.CharField(_("Description"), max_length=150)
    default_amount = models.DecimalField(_("Default Amount"), max_digits=5, decimal_places=2)
    default = models.DecimalField(_("Default %"), max_digits=5, decimal_places=2)
    exempt_amount = models.DecimalField(_("Exempt Amount"), max_digits=5, decimal_places=2)
    exempt = models.DecimalField(_("Exempt %"), max_digits=5, decimal_places=2)
    minimum_taxable =  models.DecimalField(_("Minimum Taxable"), max_digits=5, decimal_places=2)
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    percentage = models.DecimalField(_("Percentage"), max_digits=5, decimal_places=2)
    tax_type = models.CharField(_("Tax Type"), choices=text_options.TaxType.choices, max_length=50)
    bonus_tax_rate = models.DecimalField(_("Bonus Tax Rate"), max_digits=5, decimal_places=2)
    per_of_periodic_salary = models.DecimalField(_("Percentage of Periodic Salary"), max_digits=5, decimal_places=2)
    annual_bonus_tresh_hold = models.DecimalField(_("Annual Bonus Tresh Hold"), max_digits=5, decimal_places=2)
    overtime_tresh_hold = models.DecimalField(_("Overtime Tresh Hold"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Tax Laws"
        verbose_name_plural = "Tax Laws"

    def __str__(self) -> str:
        return self.no


class TaxReliefs(models.Model):
    no = models.CharField(_("No."), max_length=50)
    description = models.CharField(_("Description"), max_length=150)
    relief_type = models.CharField(_("Relief Type"), max_length=50)
    relief_value = models.DecimalField(_("Relief Value"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Tax Reliefs"
        verbose_name_plural = "Tax Reliefs"


class Currency(models.Model):
    code = models.CharField(_("Code"), max_length=50)

    def __str__(self) -> str:
        return self.code
