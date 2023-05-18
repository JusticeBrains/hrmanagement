from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from datetime import datetime


class EmployeeRequisition(models.Model):
    department = models.ForeignKey(
        "employee.Department", verbose_name=_("Department"), on_delete=models.DO_NOTHING
    )
    position = models.ForeignKey("company.JobTitles", verbose_name=_("Position"), on_delete=models.DO_NOTHING)
    no_of_vacancies = models.PositiveIntegerField(_("No Of Vacancies"))

    class Meta:
        verbose_name = "Employee Requisition"
        verbose_name_plural = "Employee Requisitions"

    def __str__(self) -> str:
        return f"{self.department} - {self.position} - {self.no_of_vacancies}"

    def __repr__(self) -> str:
        return f"{self.department} - {self.position} - {self.no_of_vacancies}"


class JobRequirements(models.Model):
    employee_requisition = models.ForeignKey(
        "recruitment.EmployeeRequisition",
        verbose_name=_("Employee Requisition"),
        on_delete=models.CASCADE,
        related_name="requirement_requisistion",
    )
    requirement_name = ArrayField(
        base_field=models.CharField(_("Requirement"), max_length=150),
        blank=True,
        null=True,
    )
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = "Job Requirement"
        verbose_name_plural = "Job Requirements"

    def __str__(self):
        return f"{self.requirement_name[:50]} - {self.description[:50]}"

    def __repr__(self):
        return f"{self.requirement_name[:50]} - {self.description[:50]}"


class JobApplication(models.Model):
    employee_requisition = models.ForeignKey(
        "recruitment.EmployeeRequisition",
        verbose_name=_("Employee Requisition"),
        on_delete=models.CASCADE,
        related_name="application_requisistion",
    )
    applicant_firstname = models.CharField(_("Applicant FirstName"), max_length=150)
    applicant_lastname = models.CharField(_("Applicant LastName"), max_length=150)
    applicant_othername = models.CharField(_("Applicant OtherName"), max_length=150, null=True, blank=True)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=15)
    resume = models.FileField(_("Resume"), upload_to="resume/")
    cover_letter = models.TextField(_("Cover Letter"))
    status = models.CharField(_("Status"), max_length=50, default="Pending")
    year = models.CharField(_("Year"), max_length=50, default=timezone.now().year)
    short_list = models.BooleanField(_("Shorted Listed Application"), default=False)
    interviewed = models.BooleanField(_("Interviewed"), default=False)
    recruited = models.BooleanField(_("Recruited"), default=False)
    total_interview_score = models.PositiveIntegerField(
        _("Total Interviewed Score"), blank=True, null=True
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

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"

    def __str__(self):
        return f"{self.job_application} - {self.interview_date}  - {self.interview_location} - {self.interview_score}"

    def __repr__(self):
        return f"{self.job_application} - {self.interview_date}  - {self.interview_location} - {self.interview_score}"
