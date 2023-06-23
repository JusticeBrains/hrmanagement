import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.contrib.postgres.fields import IntegerRangeField


class GlobalQualification(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)
    value = models.PositiveIntegerField(_("Value"), blank=True, null=True)

    class Meta:
        verbose_name = "Global Qualification"
        verbose_name_plural = "Global Qualifications"

    def __str__(self):
        return f"{self.value} - {self.name}" if self.name else ""


class CompanyQualifications(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    # globalqualification = models.ManyToManyField(to=GlobalQualification)
    global_qualification = models.ForeignKey(
        "recruitment.GlobalQualification",
        verbose_name=_("Global Qualification"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    qualification_name = models.CharField(
        _("Qualifcation Name"), max_length=150, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Company Qualifications"
        verbose_name_plural = "Company Qualifications"

    def __str__(self):
        return str(self.company_name)


class EmployeeRequisition(models.Model):
    department = models.ForeignKey(
        "employee.Department", verbose_name=_("Department"), on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        "company.JobTitles", verbose_name=_("Position"), on_delete=models.DO_NOTHING
    )
    no_of_vacancies = models.PositiveIntegerField(_("No Of Vacancies"))
    qualifications = models.TextField(_("Qualification"), null=True, blank=True)
    status = models.CharField(_("Status"), default=0, max_length=50)
    created_at = models.DateField(
        _("Created At"), auto_now_add=True, null=True, blank=True
    )
    requirement_name = ArrayField(
        base_field=models.CharField(_("Requirement"), max_length=150),
        blank=True,
        null=True,
    )
    description = models.TextField(_("Description"), null=True, blank=True)
    published = models.PositiveIntegerField(_("Published"), default=0)
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.CharField(
        _("Company ID"), max_length=150, blank=True, null=True
    )
    age_limits = IntegerRangeField(blank=True, null=True)
    years_of_experience = IntegerRangeField(blank=True, null=True)
    unique_code = models.CharField(
        _("Unique Code"), max_length=50, null=True, blank=True
    )
    company_qualifications = models.ForeignKey(
        "recruitment.CompanyQualifications",
        verbose_name=_("Company Qualifications"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    published_date = models.DateField(
        _("Published Date"), auto_now=False, auto_now_add=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Employee Requisition"
        verbose_name_plural = "Employee Requisitions"

    @staticmethod
    def get_age_for_shortlisting(age):
        if age is not None:
            age_limit = EmployeeRequisition.objects.filter(
                age_limits__contains=age
            ).first()
            return age_limit
        return None

    @staticmethod
    def get_years_of_experience_for_shortlisting(year):
        if year is not None:
            experience_years = EmployeeRequisition.objects.filter(
                years_of_experience__contains=year
            ).first()
            return experience_years
        return None

    def __str__(self) -> str:
        return f"{self.department} - {self.position} - {self.no_of_vacancies}"

    def __repr__(self) -> str:
        return f"{self.department} - {self.position} - {self.no_of_vacancies}"


class JobApplication(models.Model):
    employee_requisition = models.ForeignKey(
        "recruitment.EmployeeRequisition",
        verbose_name=_("Employee Requisition"),
        on_delete=models.CASCADE,
        related_name="application_requisistion",
        null=True,
        blank=True,
    )
    applicant_firstname = models.CharField(_("Applicant FirstName"), max_length=150)
    applicant_lastname = models.CharField(_("Applicant LastName"), max_length=150)
    applicant_othername = models.CharField(
        _("Applicant OtherName"), max_length=150, null=True, blank=True
    )
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=15, blank=True, null=True)
    resume = models.TextField(_("Resume"), blank=True, null=True)
    cover_letter = models.TextField(_("Cover Letter"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=50, default="Pending")
    year = models.CharField(_("Year"), max_length=50, default=timezone.now().year)
    short_list = models.BooleanField(_("Shorted Listed Application"), default=False)
    interviewed = models.BooleanField(_("Interviewed"), default=False)
    recruited = models.BooleanField(_("Recruited"), default=False)
    total_interview_score = models.PositiveIntegerField(
        _("Total Interviewed Score"), blank=True, null=True
    )
    date_of_brith = models.DateField(
        _("Date Of Birth"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    age = models.PositiveIntegerField(_("Age"), blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(
        _("Years Of Experience"), default=0
    )
    system_shortlisted = models.BooleanField(
        _("System Shortlisted"), blank=True, null=True
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.CharField(
        _("Company ID"), max_length=150, blank=True, null=True
    )
    company_qualifications = models.ForeignKey(
        "recruitment.CompanyQualifications",
        verbose_name=_("Company Qualifications"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    qualifications = models.CharField(
        _("Qualification"), null=True, blank=True, max_length=50
    )
    date_of_application = models.DateField(
        _("Date Of Application"),
        auto_now=False,
        auto_now_add=False,
        auto_created=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"

    @property
    def fullname(self):
        if self.applicant_othername:
            return f"{self.applicant_lastname}, {self.applicant_firstname} {self.applicant_othername}"
        return f"{self.applicant_lastname}, {self.applicant_firstname}"

    def __str__(self):
        return f"{self.fullname} - {self.status}"

    def __repr__(self):
        return f"{self.fullname} - {self.status}"


class ApplicantQualification(models.Model):
    job_application = models.ForeignKey(
        "recruitment.JobApplication",
        verbose_name=_("Job Application"),
        on_delete=models.CASCADE,
        related_name="qualification_application",
    )
    qualification_name = models.CharField(
        _("Qualification"), max_length=150, blank=True, null=True
    )
    attachment = models.TextField(_("Attachment"))
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Applicant Qualification"
        verbose_name_plural = "Applicant Qualifications"

    def __str__(self):
        return f"{self.job_application} - {self.qualification_name}"

    def __repr__(self):
        return f"{self.job_application} - {self.qualification_name}"


class Interview(models.Model):
    job_application = models.ForeignKey(
        "recruitment.JobApplication",
        verbose_name=_("Job Application"),
        on_delete=models.CASCADE,
        related_name="interview_application",
    )
    panelist_name = models.CharField(
        _("Panelist Name"), max_length=250, blank=True, null=True
    )
    interview_date = models.DateField(_("Interview Date"), default=timezone.now)
    interview_time = models.TimeField(_("Interview Time"), auto_now_add=False)
    interview_location = models.CharField(
        _("Interview Location"), max_length=150, blank=True, null=True
    )
    interview_score = models.PositiveIntegerField(
        _("Interview Score"), blank=True, null=True
    )
    interview_comments = models.TextField(
        _("Interview Comments"), blank=True, null=True
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"

    def __str__(self):
        return f"{self.job_application} - {self.interview_date}  - {self.interview_location} - {self.interview_score}"

    def __repr__(self):
        return f"{self.job_application} - {self.interview_date}  - {self.interview_location} - {self.interview_score}"
