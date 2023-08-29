from django.db import models
import uuid
import random

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model  # get current active user
from django.conf import settings  # get a user
from django.utils import timezone
from options import text_options
from employee.models import Employee
User = get_user_model()


class CompanyAdmin(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(
        _("First Name"), max_length=150, null=True, blank=True
    )
    last_name = models.CharField(_("Last Name"), max_length=150, blank=True, null=True)
    password = models.CharField(_("Password"), max_length=150, null=True, blank=True)
    company_id = models.OneToOneField(
        "company.Company", verbose_name=_("Company"), on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = "Company Admin"
        verbose_name_plural = "Company Admin"


class Company(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Company Name"), max_length=150)
    comp_type = models.ForeignKey(
        "CompanyType",
        verbose_name=_("Company Type"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    unique_code = models.CharField(
        _("Unique Code"), max_length=50, null=True, blank=True
    )
    logo = models.TextField(_("Logo"), blank=True, null=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"
    
    def update_employee(self):
        Employee.objects.filter(company_id=self).update(unique_code=self.unique_code)
    
    def save(self, *args, **kwargs):
        self.update_employee()
        super().save(*args, **kwargs)

    @property
    def alias(self):
        return f"{self.name[:3]}{random.randint(300,9000)}"


class CompanyType(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    type = models.CharField(_("Company Type"), max_length=50)

    class Meta:
        verbose_name = "Company Type"
        verbose_name_plural = "Company Types"

    def __str__(self):
        return f"{self.type}"


class Holidays(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    holiday = models.CharField(_("Holiday"), max_length=50)

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"

    def __str__(self):
        return f"{self.holiday}, {self.date}"


class PayrollStructure(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=150, blank=True, null=True)
    year = models.PositiveIntegerField(_("Year"))
    name = models.CharField(_("Name"), max_length=150)
    start_date = models.DateField(
        _("Start Date"),
    )
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    closed = models.BooleanField(_("Closed"), default=False)
    company = models.CharField(_("Company"), max_length=150, null=True, blank=True)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.DO_NOTHING,
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

    class Meta:
        verbose_name = "Payroll Structure"
        verbose_name_plural = "Payroll Structures"
    
    def __str__(self) -> str:
        return f"{self.code}"
    
    def populate_fields(self):
        self.company = self.company_id.name if self.company_id is not None else None

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)
    

class BaseCom(models.Model):
    id = models.UUIDField(_("ID"), default=uuid.uuid4, primary_key=True, editable=False)
    code = models.CharField(_("Code"), max_length=150, blank=True, null=True)
    payroll_structure = models.ForeignKey("company.PayrollStructure", verbose_name=_("Payroll Structure"), on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    class Meta:
        abstract = True


class JobTitles(BaseCom):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    description = models.CharField(_("Description"), max_length=80)
    company = models.CharField(_("Company"), max_length=150, null=True, blank=True)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Job Titles"
        verbose_name_plural = "Job Titles"

    def __str__(self):
        return f"{self.code} - {self.description}"

    def populate_fields(self):
        self.company = self.company_id.name if self.company_id is not None else None

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)

# if connection.vendor == 'postgresql':
#     with connection.cursor() as cursor:
#         cursor.execute("""
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'company_jobtitles' AND column_name = 'code'
#             )
#         """)
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute("ALTER TABLE company_jobtitles ALTER COLUMN code TYPE VARCHAR(50)")


class SalaryGrade(BaseCom):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    job_titles = models.ForeignKey("company.JobTitles", verbose_name=_("Job Titles"), on_delete=models.CASCADE, blank=True, null=True)
    company = models.CharField(_("Company"), max_length=150, null=True, blank=True)
    company_id = models.CharField(_("Company ID"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Salary Grade"
        verbose_name_plural = "Salary Grades"

    def __str__(self) -> str:
        return f"{self.code} - {self.payroll_structure}"

    def populate_company(self):
        self.company = self.payroll_structure.company if self.payroll_structure is not None else None
        self.company_id = self.payroll_structure.id if self.payroll_structure is not None else None

    def save(self, *args, **kwargs):
        self.populate_company()
        super().save(*args, **kwargs)   

# if connection.vendor == 'postgresql':
#     with connection.cursor() as cursor:
#         cursor.execute("""
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'company_salarygrade' AND column_name = 'code'
#             )
#         """)
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute("ALTER TABLE company_salarygrade ALTER COLUMN code TYPE VARCHAR(50)")


class Policy(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    heading = models.CharField(_("Heading"), max_length=250, blank=True, null=True)
    details = models.TextField(_("Details"), blank=True, null=True)
    company = models.ForeignKey(
        "company.Company", verbose_name=_("Company"), on_delete=models.CASCADE
    )
    date = models.DateField(_("Date"), default=timezone.now)
    published = models.BooleanField(_("Published"), default=False)

    class Meta:
        verbose_name = "Policy"
        verbose_name_plural = "Policies"

    def __str__(self) -> str:
        return f"{self.heading}"


class EmployeePolicy(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    employee = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE, blank=True, null=True
    )
    policy = models.ForeignKey(
        "company.Policy", verbose_name=_("Policy"), on_delete=models.CASCADE, blank=True
    )
    date = models.DateField(_("Date"), default=timezone.now)
    accepted = models.BooleanField(_("Accepted"), default=False)

    class Meta:
        verbose_name = "Employee Policy"
        verbose_name_plural = "Employee Policies"

    def __str__(self) -> str:
        return f"{self.employee}"


class DepartmentPolicy(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    department = models.ForeignKey(
        "employee.Department", verbose_name=_("Department"), on_delete=models.CASCADE, blank=True, null=True
    )
    policy = models.ForeignKey(
        "company.Policy", verbose_name=_("Policy"), on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField(_("Date"), default=timezone.now)
    accepted = models.BooleanField(_("Accepted"), default=False)

    class Meta:
        verbose_name = "Department Policy"
        verbose_name_plural = "Department Policies"

    def __str__(self) -> str:
        return f"{self.department}"


class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"


class BankBranch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Branch Name"), max_length=150, blank=True, null=True)
    bank = models.ForeignKey(
        "company.Bank",
        verbose_name=_("Bank"),
        on_delete=models.CASCADE,
        related_name="branches",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Bank Branch"
        verbose_name_plural = "Bank Branches"