from collections.abc import Iterable
import uuid
from options.text_options import (
    AppraisalSetUpType,
    DisbursementType,
    ReviewType,
    OffenseType,
    RecommendedAction,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.postgres.fields import IntegerRangeField

User = get_user_model()


class Employee(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80)
    gender = models.CharField(_("Gender"), max_length=50, blank=True, null=True)
    phone_no2 = models.CharField(
        _("Phone Number 2"), max_length=50, blank=True, null=True
    )
    company_email = models.EmailField(
        _("Company Email"), max_length=254, blank=True, null=True
    )
    job_titles = models.ForeignKey(
        "company.JobTitles",
        verbose_name=_("Job Titles"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    job_title_description = models.CharField(
        _("Job Title Description"), max_length=250, null=True, blank=True
    )
    privacy_blocked = models.CharField(
        _("Privacy Blocked"), max_length=50, blank=True, null=True
    )
    address = models.CharField(_("Address"), max_length=250, blank=True, null=True)
    address_2 = models.CharField(_("Address 2"), max_length=250, blank=True, null=True)
    post_code = models.CharField(_("Post Code"), max_length=250, blank=True, null=True)
    city = models.CharField(_("City"), max_length=250, blank=True, null=True)
    country_region_code = models.CharField(
        _("Country Region Code"), max_length=50, blank=True, null=True
    )
    showmap = models.CharField(_("Show Map"), max_length=250, blank=True, null=True)
    mobile_no = models.CharField(max_length=250, null=True, blank=True)
    pager = models.CharField(_("Pager"), max_length=250, blank=True, null=True)
    extension = models.CharField(_("Extension"), max_length=250, blank=True, null=True)
    email = models.CharField(_("Email"), max_length=150, blank=True, null=True)
    alt_address_code = models.CharField(
        _("Alt Address Code"), max_length=250, blank=True, null=True
    )
    alt_address_start_date = models.CharField(
        _("Alt Address Start Date"), max_length=250, blank=True, null=True
    )
    alt_address_end_date = models.CharField(
        _("Alt Address End Date"), max_length=250, blank=True, null=True
    )
    department = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    department_name = models.CharField(
        _("Department Name"), max_length=250, blank=True, null=True
    )
    unit = models.ForeignKey(
        "employee.Unit",
        verbose_name=_("Unit"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    unit_name = models.CharField(_("Unit Name"), max_length=250, blank=True, null=True)
    branch = models.ForeignKey(
        "employee.Branch",
        verbose_name=_("Branch"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    branch_name = models.CharField(
        _("Branch Name"), max_length=250, blank=True, null=True
    )
    fifth_category_level = models.CharField(
        _("Fifth Category Level"), max_length=250, blank=True, null=True
    )
    employment_date = models.CharField(
        _("Employement Date"), max_length=250, blank=True, null=True
    )
    status = models.CharField(_("Status"), max_length=250, blank=True, null=True)
    inactive_date = models.CharField(
        _("Inactive Date"), max_length=250, blank=True, null=True
    )
    cause_of_inactivity_code = models.CharField(
        _("Cause of Inactive Code"), max_length=250, blank=True, null=True
    )
    termination_date = models.CharField(
        _("Termination Date"), max_length=250, blank=True, null=True
    )
    employement_contract_code = models.CharField(
        _("Employement Contract Code"), max_length=250, blank=True, null=True
    )
    resource_no = models.CharField(
        _("Resource No"), max_length=250, blank=True, null=True
    )
    salesperson_purch_code = models.CharField(
        _("Salespers Purch Code"), max_length=250, null=True, blank=True
    )
    birth_date = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    ssno = models.CharField(
        _("Social Security No"), max_length=50, blank=True, null=True
    )
    union_code = models.CharField(_("Union Code"), max_length=50, null=True, blank=True)
    union_membership_number = models.CharField(
        _("Union Membership Number"), max_length=50, null=True, blank=True
    )
    employee_posting_group = models.CharField(
        _("Employee Posting Code"), max_length=50, blank=True, null=True
    )
    application_method = models.CharField(
        _("Application Method"), max_length=50, null=True, blank=True
    )
    pay_group_code = models.ForeignKey(
        "employee.PayGroup",
        verbose_name=_("Pay Group Code"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    pay_group_name = models.CharField(
        _("Pay Group Name"), max_length=250, blank=True, null=True
    )
    salary_grade = models.ForeignKey(
        "company.SalaryGrade",
        verbose_name=_("Salary Grade"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    notch = models.ForeignKey(
        "employee.Notch",
        verbose_name=_("Notch"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    annual_basic = models.CharField(
        _("Annual Basic"), max_length=50, blank=True, null=True
    )
    contribute_to_ssf_employee = models.CharField(
        _("Contribute TO SSF Employee"), max_length=50, blank=True, null=True
    )
    contribute_to_ssf_employer = models.CharField(
        _("Contribute TO SSF Employer"), max_length=50, blank=True, null=True
    )
    payment_mode = models.CharField(
        _("Payment Mode"), max_length=50, blank=True, null=True
    )
    payment_method = models.CharField(
        _("Payment Method"), max_length=50, blank=True, null=True
    )
    bank_id = models.ForeignKey(
        "company.Bank",
        verbose_name=_("Bank"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    bank_name = models.CharField(_("Bank Name"), max_length=150, blank=True, null=True)
    bank_branch_id = models.ForeignKey(
        "company.BankBranch",
        verbose_name=_("Bank Branch"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    bank_branch_name = models.CharField(
        _("Bank Branch Name"), max_length=150, blank=True, null=True
    )
    bank_account_no = models.CharField(
        _("Bank Account No"), max_length=50, blank=True, null=True
    )
    currency = models.CharField(_("CUrrency"), max_length=50, null=True, blank=True)
    iban = models.CharField(_("IBAN"), max_length=50, null=True, blank=True)
    swift_code = models.CharField(_("Swift Code"), max_length=50, blank=True, null=True)
    phone_no = models.CharField(_("Phone Number"), max_length=50, blank=True, null=True)
    grounds_for_term = models.CharField(
        _("Grounds For Termination"), max_length=50, blank=True, null=True
    )
    employee_level = models.CharField(
        _("Employee Level"), max_length=50, blank=True, null=True
    )
    profile_pic = models.TextField(_("Profile Pic"), null=True, blank=True)
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    unique_code = models.CharField(
        _("Unique Code"), max_length=50, null=True, blank=True
    )
    medical_claim_amount_left = models.PositiveIntegerField(
        _("Medical Claim Amount Left"), blank=True, null=True
    )
    used_medical_claim_amount = models.PositiveIntegerField(
        _("Used Medical Claim Amoun"), null=True, blank=True
    )
    total_medical_claim_amount = models.PositiveIntegerField(
        _("Total Medical Claim"), null=True, blank=True
    )
    is_super = models.PositiveIntegerField(_("Is Super"), default=0)
    is_hr = models.PositiveIntegerField(_("Is Hr"), default=0)
    is_super_hr = models.PositiveIntegerField(_("Is Super HR"), default=0)
    is_accountant = models.PositiveIntegerField(
        _("Is Accountant"), blank=True, null=True, default=0
    )
    is_gm = models.PositiveIntegerField(_("Is GM"), default=0)
    net_salary = models.DecimalField(
        _("Net Salary"), max_digits=10, decimal_places=4, default=0.0
    )
    gross_salary = models.DecimalField(
        _("Gross Salary"), max_digits=10, decimal_places=4, default=0.0
    )

    class Meta:
        unique_together = ("code", "company")
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        if self.middle_name:
            return (
                f"{self.last_name}, {self.first_name} {self.middle_name} - {self.code}"
            )
        return f"{self.last_name} {self.first_name} {self.code}"

    def __repr__(self):
        if self.middle_name:
            return (
                f"{self.last_name}, {self.first_name} {self.middle_name} - {self.code}"
            )
        return f"{self.last_name} {self.first_name} {self.code}"

    @property
    def fullname(self):
        if self.middle_name:
            return f"{self.last_name}, {self.first_name} {self.middle_name}"
        return f"{self.last_name}, {self.first_name}"


class EmployeeDeduction(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    employee = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    no_of_days = models.PositiveIntegerField(
        _("No Of Days To Be Deducted"), blank=True, null=True
    )
    deduction_reason = models.CharField(
        _("Deduction Reason"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Employee Deduction"
        verbose_name_plural = "Employee Deductions"

    def __str__(self):
        return f"{self.employee.fullname} - {self.deduction_reason} - {self.no_of_days}"


class AppraisalSetup(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    appraisal_type = models.CharField(
        _("Appraisal Type"),
        choices=AppraisalSetUpType.choices,
        max_length=50,
        blank=True,
        null=True,
    )
    appraisal_id = models.CharField(_("Global Name"), max_length=150, blank=True, null=True)
    appraisal_name = models.CharField(
        _("Appraisal Name"), max_length=50, blank=True, null=True
    )
    appraisal_date = models.DateField(
        _("Appraisal Date"), default=timezone.now, blank=True, null=True
    )
    appraiser = models.CharField(
        verbose_name="Appraiser", max_length=200, blank=True, null=True
    )
    status = models.PositiveIntegerField(_("Status"), default=0)
    period = models.CharField(_("Period"), max_length=150, default=timezone.now().year)
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Appraisal SetUp"
        verbose_name_plural = "Appraisal SetUps"

    def __str__(self):
        return f"{self.appraisal_name}"
    def save(self, *args, **kwargs):
        self.company = self.company_id.name
        return super().save(*args, **kwargs)


class EmployeeAppraisal(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    appraisal_setup = models.ForeignKey("employee.AppraisalSetup", verbose_name=_("Appraisal SetUp"), on_delete=models.CASCADE)
    emp_id = models.ForeignKey(
        Employee,
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        related_name="emp_id",
        null=True,
    )
    emp_name = models.CharField(
        verbose_name=_("Employee Name"),
        max_length=150,
        null=True,
        blank=True,
        editable=False,
    )
    employee_code = models.CharField(
        _("Employee Code"), max_length=50, blank=True, null=True, editable=False
    )
    job_title = models.CharField(
        _("Job Title"), max_length=150, null=True, blank=True, editable=False
    )
    appraisal_date = models.DateField(
        _("Appraisal Date"), default=timezone.now, blank=True, null=True
    )
    appraiser = models.CharField(
        verbose_name="Appraiser", max_length=200, blank=True, null=True
    )
    department = models.CharField(
        _("Department"), max_length=250, null=True, blank=True
    )
    department_id = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    grade = models.CharField(_("Grade"), max_length=150, null=True, blank=True)
    performance_score = models.DecimalField(
        _("Performance Score"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    appraisal_score = models.DecimalField(
        _("Appraisal Score"), max_digits=5, decimal_places=2, null=True, blank=True
    )
    behavioural_score = models.DecimalField(
        _("Behavioural Score"), max_digits=5, decimal_places=2, null=True, blank=True
    )
    percentage_score = models.CharField(
        _("Percentage Score"), null=True, blank=True, max_length=50
    )
    status = models.PositiveIntegerField(_("Status"), default=0)
    period = models.CharField(_("Period"), max_length=150, default=timezone.now().year)
    recommendation = models.CharField(
        _("Recommendation"), max_length=150, blank=True, null=True
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    weighted_score = models.PositiveIntegerField(
        _("Weighted Score"), blank=True, null=True
    )
    weighted_behavioural_score = models.PositiveIntegerField(
        _("Weighted Behavioural Score"), null=True, blank=True
    )
    hr_status = models.PositiveIntegerField(_("HR Status"), default=0)
    emp_comment = models.TextField(_("Employee Comment"), blank=True, null=True)
    improvement_needs = models.TextField(_("Improvement Needs"), blank=True, null=True)
    improvement_plan = models.TextField(_("Improvement Plan"), blank=True, null=True)

    class Meta:
        verbose_name = "Employee Appraisal"
        verbose_name_plural = "Employee Appraisals"

    def __str__(self) -> str:
        return f"{self.emp_name} {self.employee_code} - {self.grade}"


class AppraisalGrading(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    score_range = IntegerRangeField(blank=True, null=True)
    grade = models.CharField(_("Grade"), max_length=50, null=True, blank=True)
    recommendation = models.CharField(
        _("Recommendation"), max_length=150, blank=True, null=True
    )
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Appraisal Grading"
        verbose_name_plural = "Appraisal Gradings"

    @staticmethod
    def get_grading_for_score(score):
        if score is not None:
            grading = AppraisalGrading.objects.filter(
                score_range__contains=score
            ).first()
            return grading
        return None

    def __str__(self) -> str:
        return f"{self.grade} - {self.recommendation}"

    def clean(self):
        self.company = self.company_id.name


class KPI(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    period = models.CharField(_("Period"), max_length=150, default=timezone.now().year)
    kpi_area = models.CharField(
        _("KPI/Appraisal Areas"), max_length=250, blank=True, null=True
    )
    supervisor_score = models.DecimalField(
        _("Supervisor Score in Pecentage %"),
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )
    emp_score = models.IntegerField(
        _("Employee Score in Pecentage %"), blank=True, null=True
    )
    emp_comment = models.CharField(
        _("Employee Comment"), max_length=50, null=True, blank=True
    )
    supervisor_comment = models.CharField(
        _("Supervisor Comment"), max_length=50, null=True, blank=True
    )
    employee_id = models.ForeignKey(
        Employee,
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        related_name="employee_kpi",
        null=True,
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.CharField(
        _("Company ID"), max_length=150, null=True, blank=True
    )
    kpi_score = models.DecimalField(
        _("KPI Score"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    employee_kra = models.ForeignKey(
        "employee.EmployeeKRA",
        verbose_name=_("Employee KRA"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    score = models.DecimalField(
        _("Percentage Score"), max_digits=5, decimal_places=2, null=True, blank=True
    )
    supervisor_status = models.PositiveIntegerField(_("Supervisor Status"), default=0)
    employee_status = models.PositiveIntegerField(_("Supervisor Status"), default=0)

    def clean(self):
        if self.employee_id:
            self.company = self.employee_id.company

        # if self.score > self.kpi_score:
        #     raise ValidationError(
        #         f"Score {self.score} cannot be greater than kpi score{self.kpi_score}"
        #     )
        # if self.score is not None:
        #     self.percentage_score = round((self.score / 100)*self.kpi_score, ndigits=2)

    class Meta:
        verbose_name = "KPI"
        verbose_name_plural = "KPI's"

    def __str__(self):
        return f"{self.period} - {self.employee_id.fullname}"


class EmployeeKRA(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)
    total_score = models.PositiveIntegerField(_("Total Score"), blank=True, null=True)
    period = models.CharField(_("Period"), max_length=150, default=timezone.now().year)
    employee_id = models.ForeignKey(
        Employee,
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        related_name="employee_kra",
        null=True,
    )
    emp_code = models.CharField(
        _("Employee Code"), max_length=150, null=True, blank=True, editable=False
    )
    emp_name = models.CharField(
        _("Employee Name"), max_length=150, null=True, blank=True, editable=False
    )
    appraiser = models.CharField(_("Appraiser"), max_length=150, null=True, blank=True)
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    appraiser = models.CharField(_("Appraiser"), max_length=150, null=True, blank=True)
    status = models.PositiveIntegerField(_("Status"), default=0)
    due_date = models.DateField(_("Due Date"), blank=True, null=True)
    department = models.CharField(
        _("Department"),
        max_length=150,
        null=True,
        blank=True,
    )
    department_id = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    narration = models.CharField(_("Narration"), max_length=250, blank=True, null=True)
    target = models.CharField(_("Target"), max_length=150, blank=True, null=True)
    emp_total_score = models.DecimalField(
        _("Employee Total Score"), max_digits=5, decimal_places=2, null=True, blank=True
    )
    supervisor_total_score = models.DecimalField(
        _("Supervisor Total Score"),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    computed_supervisor_score = models.DecimalField(
        _("Computed Supervisor Score"), max_digits=5, decimal_places=2, default=0
    )
    computed_employee_score = models.DecimalField(
        _("Computed Employee Score"), max_digits=5, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = "Employee KRA"
        verbose_name_plural = "Employee KRA's"

    def __str__(self):
        return f"{self.name} - {self.period}"

    # def clean(self) -> None:
    #     kpi_scores_sum = self.kpis.aggregate(sum_scores=models.Sum("kpi_scores"))[
    #         "sum_scores"
    #     ]

    #     if kpi_scores_sum != self.total_score:
    #         raise ValidationError(
    #             f"Sum Of Total KPI Scores not equal to KRA Total Score"
    #         )

    # def create_kpis(
    #     self,
    #     # kpi_appraisal_area,
    #     # kpi_appraisal_area_description,
    #     kpi_score,
    #     employee_id,

    # ):
    #     kpi_item = KPI.objects.create(
    #         employee_kra=self,
    #         # kpi_appraisal_area=kpi_appraisal_area,
    #         # kpi_appraisal_area_description=kpi_appraisal_area_description,
    #         employee_id=employee_id,
    #         kpi_score=kpi_score,
    #     )
    #     return kpi_item


class EmployeeMedicalClaim(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    employee_id = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    emp_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    department = models.CharField(
        _("Department"), max_length=150, blank=True, null=True
    )
    department_id = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department ID"),
        on_delete=models.DO_NOTHING,
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)
    company_id = models.ForeignKey(
        "company.Company", verbose_name=_("Company ID"), on_delete=models.DO_NOTHING
    )
    claim_amount = models.PositiveIntegerField(_("Claim Amount"), blank=True, null=True)
    claim_reason = models.TextField(_("Claim Reason"), blank=True, null=True)
    supporting_doc1 = models.TextField(
        _("Supporting Document 1"), blank=True, null=True
    )
    supporting_doc2 = models.TextField(
        _("Supporting Document 2"), blank=True, null=True
    )
    status = models.PositiveIntegerField(_("Status"), blank=True, null=True, default=0)
    validation_status = models.PositiveIntegerField(
        _("Validation Status"), blank=True, null=True, default=0
    )
    validated_by = models.CharField(
        _("Validated By"), max_length=150, blank=True, null=True
    )
    validation_date = models.DateField(
        _("Validation Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    processed_status = models.PositiveIntegerField(
        _("Processed Status"), blank=True, null=True, default=0
    )
    processed_by = models.CharField(
        _("Processed By"), max_length=150, blank=True, null=True
    )
    processed_date = models.PositiveIntegerField(
        _("Processed Date"), blank=True, null=True
    )
    period = models.CharField(_("Period"), max_length=150, default=timezone.now().year)
    created_at = models.DateField(_("Created At"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Employee Medical Claim"
        verbose_name_plural = "Employee Medical Claims"

    def __str__(self):
        return f"{self.emp_name} - {self.claim_amount} - {self.created_at}"


class EmployeePayReview(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    no = models.CharField(_("Code"), max_length=50)
    review_type = models.CharField(
        _("Review Type"),
        choices=ReviewType.choices,
        default=ReviewType.ANNUAL_REVIEW,
        max_length=50,
    )
    emp_code = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE
    )
    emp_name = models.CharField(_("Employee Name"), max_length=150)
    job_title_code = models.CharField(_("Job Title Code"), max_length=150)
    job_title = models.CharField(_("Job Title"), max_length=150)
    base_pay = models.DecimalField(_("BasePay"), max_digits=5, decimal_places=2)
    percentage_increase = models.DecimalField(
        _("Percentage Increase"), max_digits=5, decimal_places=2
    )
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    effective_date = models.DateField(
        _("Effective Date"), auto_now=True, auto_now_add=False
    )
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=False, auto_now_add=False
    )
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Employee Pay Review"
        verbose_name_plural = "Employee Pay Reviews"

    @property
    def new_base_pay(self):
        return round(
            (self.base_pay + ((self.base_pay * self.percentage_increase) / 100)), 2
        )

    def __str__(self):
        return self.new_base_pay


class Base(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=50, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)
    comp_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Comp ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    company_id = models.CharField(
        _("Company ID"), max_length=150, blank=True, null=True
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)

    class Meta:
        unique_together = ("code", "company")
        abstract = True


class StaffCategory(Base):
    max_number_of_days = models.PositiveIntegerField(_("Max Number Of Days"))

    class Meta:
        verbose_name = "Staff Category"
        verbose_name_plural = "Staff Categories"

    def __str__(self):
        return f"{self.code} - {self.name} - {self.max_number_of_days}"


# # Set the data type of the primary key to VARCHAR in PostgreSQL
# if connection.vendor == "postgresql":
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'employee_staffcategory' AND column_name = 'code'
#             )
#         """
#         )
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute(
#                 "ALTER TABLE employee_staffcategory ALTER COLUMN code TYPE VARCHAR(50)"
#             )


class Department(Base):
    first_category_code = models.CharField(
        _("First Category Code"), max_length=50, blank=True, null=True
    )

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.code} -{self.name} - {self.first_category_code}"


# if connection.vendor == "postgresql":
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'employee_department' AND column_name = 'code'
#             )
#         """
#         )
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute(
#                 "ALTER TABLE employee_department ALTER COLUMN code TYPE VARCHAR(50)"
#             )


class Unit(Base):
    department = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    department_name = models.CharField(
        _("Department Name"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"
        unique_together = ("code", "comp_id", "department")

    def save(self, *args, **kwargs):
        if self.department is not None:
            self.department_name = str(self.department.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.department}"


# if connection.vendor == "postgresql":
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'employee_unit' AND column_name = 'code'
#             )
#         """
#         )
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute(
#                 "ALTER TABLE employee_unit ALTER COLUMN code TYPE VARCHAR(50)"
#             )


class Branch(Base):
    unit = models.ForeignKey(
        "employee.Unit",
        verbose_name=_("Unit"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    unit_name = models.CharField(_("Unit Name"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def save(self, *args, **kwargs):
        if self.unit is not None:
            self.unit_name = str(self.unit.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.unit}"


# # Set the data type of the primary key to VARCHAR in PostgreSQL
# if connection.vendor == "postgresql":
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'employee_branch' AND column_name = 'code'
#             )
#         """
#         )
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute(
#                 "ALTER TABLE employee_branch ALTER COLUMN code TYPE VARCHAR(50)"
#             )


class Notch(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    no = models.CharField(_("No"), max_length=50, blank=True, null=True)
    payroll_structure_code = models.ForeignKey(
        "company.PayrollStructure",
        verbose_name=_("Payroll Structure"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    payroll_structure_name = models.CharField(
        _("Payroll Structure Name"), max_length=150, blank=True, null=True
    )
    salary_grade = models.ForeignKey(
        "company.SalaryGrade",
        verbose_name=_("Salary Grade"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    salary_grade_name = models.CharField(
        _("Salary Grade Name"), max_length=150, blank=True, null=True
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=8, decimal_places=2, null=True, blank=True
    )
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    company = models.CharField(_("Company"), max_length=150, null=True, blank=True)
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("User ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Notch"
        verbose_name_plural = "Notches"
        unique_together = (
            "no",
            "salary_grade",
            "company",
        )

    def __str__(self):
        return f"{self.payroll_structure_code} - {self.salary_grade} - {self.amount}"

    def populate_fields(self):
        self.salary_grade_name = (
            self.salary_grade.code if self.salary_grade is not None else None
        )
        self.payroll_structure_name = (
            self.payroll_structure_code.name
            if self.payroll_structure_code is not None
            else None
        )
        self.company = self.company_id.name if self.company_id is not None else None

    def save(self, *args, **kwargs):
        self.populate_fields()
        super().save(*args, **kwargs)


class PayGroup(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    no = models.CharField(_("No"), max_length=150, blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=100, null=True, blank=True
    )
    taxable_income_code = models.CharField(
        _("Taxable Income Code"), max_length=50, null=True, blank=True
    )
    taxable_income_description = models.CharField(
        _("Taxable Income Description"), max_length=100, null=True, blank=True
    )
    tax_description = models.CharField(
        _("Tax Description"), max_length=150, null=True, blank=True
    )
    gross_income_description = models.CharField(
        _("Gross Income Description"), max_length=150, null=True, blank=True
    )
    currency_code = models.CharField(
        verbose_name=_("Currency Code"), null=True, blank=True, max_length=100
    )
    bonus_tax_description = models.CharField(
        _("Bonus Tax Description"), max_length=150, null=True, blank=True
    )
    gross_up = models.BooleanField(_("Gross Up"), null=True, blank=True)
    total_medical_claim_amount = models.PositiveIntegerField(
        _("Medical Claim Amount"), null=True, blank=True
    )
    company = models.CharField(_("Comapny"), max_length=150, null=True, blank=True)
    comp_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Pay Group"
        verbose_name_plural = "Pay Groups"

    def __str__(self):
        return f"{self.no} - {self.description} - {self.taxable_income_code} - {self.company}"

    def save(self, *args, **kwargs):
        # Get the employees with the same paygroup and company
        Employee.objects.filter(pay_group_code=self, company=self.company).update(
            total_medical_claim_amount=self.total_medical_claim_amount
        )

        super().save(*args, **kwargs)


class PropertyAssignment(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    item_id = models.CharField(_("Item ID"), max_length=150, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=150, null=True, blank=True)
    value = models.CharField(_("Value"), max_length=150, null=True, blank=True)
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    employee_id = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee ID"), on_delete=models.DO_NOTHING
    )
    department_name = models.CharField(_("Department Name"), max_length=150, null=True)
    department_id = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department ID"),
        on_delete=models.DO_NOTHING,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, null=True, blank=True
    )
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    status = models.PositiveIntegerField(_("Status"), blank=True, null=True, default=0)
    status_date = models.DateField(
        _("Status Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    period = models.CharField(_("Period"), max_length=50, default=timezone.now().year)
    assigned_by = models.CharField(
        _("Assigned By"), max_length=150, blank=True, null=True
    )
    date_modified = models.DateField(
        _("Date Modified"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    date_returned = models.DateField(
        _("Date Return"), auto_now=False, auto_now_add=False, null=True, blank=True
    )
    reason_returned = models.CharField(
        _("Reason Returned"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Property Assignment"
        verbose_name_plural = "Property Assignments"

    def __repr__(self) -> str:
        return f"{self.employee_name} - {self.name} - {self.value}"


class PropertyRequest(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    description = models.TextField(_("Description"), blank=True, null=True)
    quantity = models.DecimalField(
        _("Quantity"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    value = models.DecimalField(
        _("Value"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    date_request = models.DateField(
        _("Date Requested"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    department_id = models.ForeignKey(
        "employee.Department",
        verbose_name=_("Department ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    department_name = models.CharField(
        _("Department Name"), max_length=150, blank=True, null=True
    )
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID "),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    status = models.PositiveIntegerField(_("Status"), default=0)
    expected_date = models.DateField(
        _("Expected Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    date_given = models.DateField(
        _("Date Given"), auto_now=False, auto_now_add=False, blank=True, null=True
    )

    class Meta:
        verbose_name = "Property Request"
        verbose_name_plural = "Property Requests"

    def __str__(self) -> str:
        return f"{self.description[:50]} - {self.quantity} - {self.value}"


class SupervisorRatingGuide(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    range = models.CharField(_("Range"), max_length=50, null=True, blank=True)
    score_meaning = models.CharField(
        _("Score Meaning"), max_length=250, null=True, blank=True
    )
    description = models.CharField(
        _("Description"), max_length=250, null=True, blank=True
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    company_id = models.ForeignKey(
        "company.Company", verbose_name=_("Company ID"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("SupervisorRatingGuide")
        verbose_name_plural = _("SupervisorRatingGuides")

    def __str__(self):
        return f"{self.range}, {self.score_meaning} - {self.company_name}"


class BehaviourialRatingGuide(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    score = models.PositiveIntegerField(_("Score"), blank=True, null=True)
    interpretation = models.CharField(
        _("Interpretation"), max_length=150, null=True, blank=True
    )
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Behaviourial Rating Guide"
        verbose_name_plural = "Behaviourial Rating Guide"

    def __str__(self):
        return f"{self.score}, {self.interpretation}"


class BehaviouralCompetencies(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    competency = models.CharField(
        _("Competency"), max_length=250, blank=True, null=True
    )
    target_score = models.PositiveIntegerField(_("Target Score"), default=0)
    company_id = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company ID"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    company_name = models.CharField(
        _("Company Name"), max_length=150, blank=True, null=True
    )
    period = models.CharField(_("Period"), max_length=50, default=timezone.now().year)

    class Meta:
        verbose_name = "Behaviourial Competencies"
        verbose_name_plural = "Behaviourial Competencies"

    def __str__(self):
        return f"{self.competency}, {self.target_score}"


class EmployeeBehavioural(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    competency = models.CharField(
        _("Competency"), max_length=150, blank=True, null=True
    )
    score_on_target = models.DecimalField(
        _("Score On Target"), max_digits=5, decimal_places=2, default=0.0
    )
    final_score = models.DecimalField(
        _("Final Score"), max_digits=5, decimal_places=2, default=0
    )
    computed_score = models.DecimalField(
        _("Computed Score"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    employee_id = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee ID"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    employee_name = models.CharField(
        _("Employee Name"), max_length=150, blank=True, null=True
    )
    period = models.CharField(_("Period"), max_length=50, default=timezone.now().year)
    created_at = models.DateField(
        _("Created At"), auto_now=False, auto_now_add=True, null=True, blank=True
    )

    class Meta:
        verbose_name = "Employee Behaviourial"
        verbose_name_plural = "Employees Behaviourials"
