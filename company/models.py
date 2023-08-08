from django.db import models
import uuid
import random

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model  # get current active user
from django.conf import settings  # get a user

from options import text_options

User = get_user_model()


class CompanyAdmin(models.Model):
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

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"

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
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    holiday = models.CharField(_("Holiday"), max_length=50)

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"

    def __str__(self):
        return f"{self.holiday}, {self.date}"



class PayrollStructure(models.Model):
    no = models.PositiveIntegerField(_("No."))
    year = models.PositiveIntegerField(_("Year"))
    name = models.CharField(_("Name"), max_length=150)
    start_date = models.DateField(
        _("Start Date"),
    )
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    closed = models.BooleanField(_("Closed"))


class BaseCom(models.Model):
    id = models.UUIDField(_("ID"), default=uuid.uuid4, primary_key=True, editable=False)
    code = models.CharField(_("Code"), max_length=150, blank=True, null=True)
    payroll_structure = models.CharField(
        verbose_name=_("Payroll Structure"), blank=True, null=True, max_length=50
    )

    class Meta:
        abstract = True


class SalaryGrade(BaseCom):
    job_titles = models.CharField(_("Job Titles"), max_length=150)
    transport_rate = models.DecimalField(
        _("Transport Rate"), max_digits=5, decimal_places=2
    )

    class Meta:
        verbose_name = "Salary Grade"
        verbose_name_plural = "Salary Grades"

    def __str__(self) -> str:
        return f"{self.code} - {self.payroll_structure}"


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


class JobTitles(BaseCom):
    salary_grade = models.CharField(
        verbose_name=_("Salary Grade"), blank=True, null=True, max_length=50
    )
    description = models.CharField(_("Description"), max_length=80)
    company = models.CharField(_("Company"), max_length=150, null=True, blank=True)
    company_id = models.ForeignKey("company.Company", verbose_name=_("Company ID"), on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = "Job Titles"
        verbose_name_plural = "Job Titles"

    def __str__(self):
        return f"{self.code} - {self.description}"


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


class Job(models.Model):
    comp_code = models.ForeignKey(
        "Company", verbose_name=_("Company Code"), on_delete=models.CASCADE
    )
    job_code = models.CharField(_("Job Code"), max_length=50)
    job_title = models.CharField(_("Job Title"), max_length=50)
    job_duties = models.CharField(_("Job Duties"), max_length=50)
    academic_qualification = models.CharField(
        _("Academic Qualification"), max_length=50
    )
    prof_tech_qualification = models.CharField(
        _("Prof/Technical Qualification"), max_length=50
    )
    key_competencies = models.CharField(_("Key Comptencies"), max_length=50)
    relevant_work_experience = models.CharField(
        _("Relevant Work Experience"), max_length=50
    )

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return f"{self.job_code}"


class FirstCategoryLevel(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    first_level = models.CharField(_("First Level"), max_length=50)

    class Meta:
        verbose_name = "First Category Level"
        verbose_name_plural = "First Category Level"

    def __str__(self) -> str:
        return self.code


class SecondCategoryLevel(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    first_category_code = models.CharField(_("First"), max_length=50)
    name = models.CharField(_("Name"), max_length=150)
    level_no = models.PositiveIntegerField(_("Level No."))

    def __str__(self) -> str:
        return self.code
