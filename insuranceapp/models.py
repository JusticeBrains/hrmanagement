from options import text_options

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class InsurancePremiumPayments(models.Model):
    no = models.CharField(_("No."), max_length=50)
    company_name = models.ForeignKey("company.Company", verbose_name=_("Company Name"), on_delete=models.CASCADE)
    insurance_type = models.CharField(_("Insurance Type"), choices=text_options.InsuranceType.choices, max_length=50)
    period_start_date = models.DateField(_("Period Start Date"), auto_now=True, auto_now_add=False)
    period_end_date = models.DateField(_("Period End Date"), auto_now=True, auto_now_add=False)
    amount_paid = models.DecimalField(_("Amount Paid"), max_digits=5, decimal_places=2)
    payment_date = models.DateField(_("Payment Date"), auto_now=True, auto_now_add=False)
    remarks = models.CharField(_("Remarks"), max_length=100)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Insurance Premium Payments"
        verbose_name_plural = "Insurance Premium Payments"


class GroupLifeInsurance(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    name_of_company = models.ForeignKey("company.Company", verbose_name=_("Name Of Company"), on_delete=models.CASCADE)
    address = models.CharField(_("Address"), max_length=50)
    telephone = models.CharField(_("Telephone"), max_length=50)
    contact_person = models.CharField(_("Contact Person"), max_length=50)
    type_of_policy = models.CharField(_("Type Of Policy"), max_length=50)
    premium = models.DecimalField(_("Premium"), max_digits=5, decimal_places=2)
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    date = models.DateField(_("Date"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Group Life Insurance"
        verbose_name_plural = "Group Life Insurances"


class GroupTravel(models.Model):
    no = models.CharField(_("No."), max_length=50)
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey("employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    job_title_code = models.ForeignKey("company.Job", verbose_name=_("Job Title Code"), on_delete=models.CASCADE)
    department_code = models.ForeignKey("company.Department", verbose_name=_("Department Code"),
                                        on_delete=models.CASCADE)
    job_level = models.CharField(_("Job Level"), max_length=50)
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=True, auto_now_add=False)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        abstract = True


class GroupInsuranceBeneficiaries(GroupTravel):
    incident = models.TextField(_("Incident"))
    policy_code = models.CharField(_("Policy Code"), max_length=50)
    policy_type = models.CharField(_("Policy Type"), max_length=50)
    insurance_company = models.CharField(_("Insurance Company"), max_length=50)

    class Meta:
        verbose_name = "Group Insurance Beneficiaries"
        verbose_name_plural = "Group Insurance Beneficiaries"


class TravelInsuranceEntry(GroupTravel):
    trip = models.CharField(_("Trip"), max_length=50)
    purpose = models.TextField(_("Purpose"))
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Travel Insurance Entry"
        verbose_name_plural = "Travel Insurance Entries"
