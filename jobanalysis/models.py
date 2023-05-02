from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from company.models import Job

from options.text_options import (
    FREQUENCY,
    SUPERVISIONTYPE,
    CONTACTTYPE,
    DEMANDTYPE,
    REQUIREMENTTYPE,

)

User = get_user_model()


class JobAnalysis(models.Model):
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE)
    emp_name = models.CharField(_("Employee Name"), max_length=50)
    job_title_code = models.ForeignKey(Job, verbose_name=_(""), on_delete=models.CASCADE, related_name="jobcode")
    job_title = models.ForeignKey(Job, verbose_name=_(""), on_delete=models.CASCADE, related_name="jobtitle")
    division = models.CharField(_("Division"), max_length=50)
    department = models.CharField(_("Department"), max_length=50)
    reports_to_code = models.CharField(_("ReportTo Code"), max_length=50)
    reports_to = models.CharField(_("Reports To"), max_length=150)
    job_purpose = models.CharField(_("Job Purpose"), max_length=50)
    prepared_by = models.CharField(_("Prepared By"), max_length=50)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    userId = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Job Analysis"
        verbose_name_plural = "Job Analysises"

    def __str__(self):
        return f"{self.job_title_code} {self.userId}"


class JobAnalysisDuties(models.Model):
    job_analysis_number = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis code"),
                                            on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry Number"))
    frequency = models.CharField(_("Frequency"), max_length=50, choices=FREQUENCY.choices)
    duties = models.CharField(_("Duties"), max_length=50)
    responsibilities = models.CharField(_("Responsibilities"), max_length=50)
    adr = models.CharField(_("Action/Decision/Resources"), max_length=50)

    class Meta:
        verbose_name = "Job Analysis Duties"
        verbose_name_plural = "Job Analysis Duties"


class JobRequirements(models.Model):
    job_analysis_number = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis code"),
                                            on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    type = models.CharField(_("Requirement Type"), max_length=50)


class JobAnalysisSupervision(models.Model):
    job_analysis_number = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis code"),
                                            on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry Number"))
    supervision_type = models.CharField(_("Supervision Type"), max_length=50, choices=SUPERVISIONTYPE.choices, )
    supervision_detail = models.CharField(_("Supervision Details"), max_length=50)

    class Meta:
        verbose_name = "Job Analysis Supervision"
        verbose_name_plural = "Job Analysis Supervisiond"


class JobAnalysisContact(models.Model):
    job_analysis_no = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis No."), on_delete=models.CASCADE)
    entry = models.PositiveIntegerField(_("Entry"))
    contact_type = models.CharField(_("Contact Type"), max_length=50, choices=CONTACTTYPE.choices)
    contact_person = models.CharField(_("Contact Person"), max_length=50)
    position = models.CharField(_("Position"), max_length=50)
    contact_no = models.CharField(_("Contact Number"), max_length=50)

    class Meta:
        verbose_name = "Job Analysis Contact"
        verbose_name_plural = "Job Analysis Contacts"


class JobAnalysisAuthorityLimit(models.Model):
    job_analysis_no = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis"), on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    authority_type = models.CharField(_("Authority Type"), max_length=50)
    authority_limit = models.CharField(_("Authority Limit"), max_length=50)

    class Meta:
        verbose_name = "Job Analysis Authority Limit"
        verbose_name_plural = "Job Analysis Authority Limits"


class JobAnalysisDemand(models.Model):
    job_analysis_no = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis No."), on_delete=models.CASCADE)
    entry = models.PositiveIntegerField(_("Entry No."))
    type = models.CharField(_("Demand Type"), max_length=50, choices=DEMANDTYPE.choices)
    description = models.CharField(_("Demand Description"), max_length=50)

    class Meta:
        verbose_name = "Job Analysis Demand"
        verbose_name_plural = "Job Analysis Demands"


class JobAnalysisRequirement(models.Model):
    job_analysis_no = models.ForeignKey("JobAnalysis", verbose_name=_("Job Analysis"), on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    type = models.CharField(_("Requirement Type"), max_length=50, choices=REQUIREMENTTYPE.choices)
    description = models.CharField(_("Description"), max_length=50)

    class Meta:
        verbose_name = "Job Analysis Requirement"
        verbose_name_plural = "Job Analysis Requirements"


class JobEvaluation(models.Model):
    entry_no = models.PositiveIntegerField(_("Entry No."))
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_(""), on_delete=models.CASCADE)
    emp_name = models.CharField(_("Employee Name"), max_length=50)
    department = models.CharField(_("Department"), max_length=50)
    job_title = models.ForeignKey(Job, verbose_name=_("Job Title"), on_delete=models.CASCADE)
    current_job_level = models.CharField(_("Current Job Level"), max_length=50)
    current_pay_range = models.PositiveIntegerField(_("Current Pay Range"))
    new_job_level = models.CharField(_("New Job Level"), max_length=50)
    new_pay_range = models.PositiveIntegerField(_("New Pay Range"))
    user_id = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    transaction_date = models.DateField(_("Transaction Code"), auto_now=False, auto_now_add=False)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Job Evaluation"
        verbose_name_plural = "Job Evaluations"
