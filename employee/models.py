from django.db.models import DecimalField

from company.models import Job, Company
from options.text_options import (
    GENDER,
    EMPLOYEESTATUS,
    MARITALSTATUS,
    APPRAISALGRADES,
    ReviewType,
    EmployeeType,
    MEDICALLIMITTYPE,
    OffenseType,
    RecommendedAction
)

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from leave.models import LeaveRequest

User = get_user_model()


class Employee(models.Model):
    code = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER.choices, default=GENDER.Male, null=True, blank=True)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, blank=True, null=True)
    bank_branch = models.CharField(max_length=150, null=True, blank=True)
    account_number = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    employee_category = models.CharField(max_length=120, blank=True, null=True)
    ssnit_number = models.CharField(max_length=13)
    national_id = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True, blank=True)
    employement_date = models.DateField(null=True, blank=True)
    status = models.CharField(_("Status"), max_length=50, choices=EMPLOYEESTATUS.choices, default=EMPLOYEESTATUS.ACTIVE)
    nationality = models.CharField(_("Nationality"), max_length=50)
    tin = models.CharField(max_length=40, blank=True, null=True)
    hometown = models.CharField(_("HomeTown"), max_length=50, blank=True, null=True)
    region_name = models.CharField(_("Region Name"), max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    emergency_no = models.CharField(_("Emergency No"), max_length=50, blank=True, null=True)
    marital_status = models.CharField(_("Marital Status"), max_length=50, choices=MARITALSTATUS.choices,
                                      default=MARITALSTATUS.NONE)
    email = models.EmailField(null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.IntegerField(default=1)
    is_verify = models.IntegerField(default=0)
    token = models.CharField(max_length=200, null=True, blank=True)
    password_reset_code = models.CharField(max_length=200, null=True, blank=True)
    reason = models.CharField(max_length=200, blank=True, null=True)
    last_ip = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    emp_picture = models.TextField(blank=True, null=True)
    national_id_pic = models.TextField(null=True, blank=True)
    gh_post_gps = models.CharField(max_length=40, blank=True, null=True)
    company_email = models.EmailField(_("Company Email"), max_length=254, blank=True, null=True)
    cause_of_absence_filter = models.CharField(_("Cause Of Absence Filter"), max_length=50, blank=True, null=True)
    total_absence_base = models.CharField(_("Total Absence (Base)"), max_length=50, blank=True, null=True)
    grounds_for_termination_code = models.CharField(_("Grounds for Termination Code"), max_length=50, blank=True,
                                                    null=True)
    termination_date = models.DateField(_("Termination Date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.code}'

    @property
    def fullname(self):
        return f"{self.last_name}, {self.first_name}"


class AppraisalAreas(models.Model):
    description = models.CharField(_("Description"), max_length=50)
    scored = models.BooleanField(_("Scored"))

    class Meta:
        verbose_name = "Appraisal Areas"
        verbose_name_plural = "Appraisal Areas"


class EmployeeAppraisal(models.Model):
    emp_code = models.ForeignKey(Employee, verbose_name=_("Employee Code"), on_delete=models.CASCADE,
                                 related_name="emp_code")
    emp_name = models.CharField(verbose_name=_("Employee Name"), max_length=50)
    paygroup_code = models.ForeignKey("paygroup.PayGroup", verbose_name=_("Pay Groups"), on_delete=models.CASCADE, related_name="paygroup_code")
    job_title_code = models.ForeignKey("company.JobTitles", verbose_name=_("Job Title"), on_delete=models.CASCADE, blank=True, null=True)
    job_title = models.CharField(_("Job Title"), max_length=150)
    appraisal_date = models.DateField(_("Appraisal Date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    appraisal_venue = models.CharField(_("Appraisal Venue"), max_length=50, blank=True, null=True)
    appraiser = models.CharField(verbose_name="Appraiser", max_length=200, blank=True, null=True)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False, blank=True,
                                        null=True)
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"), blank=True, null=True)

    class Meta:
        verbose_name = "Employee Appraisal"
        verbose_name_plural = "Employee Appraisals"


class EmployeeAppraisalResponse(models.Model):
    appraisal_no = models.CharField(_("Appraisal No."), max_length=50)
    emp_code = models.CharField(verbose_name=_("Employee"), max_length=50)
    appraisal_code = models.CharField(verbose_name=_("Employee Appraisal Code"), max_length=50)
    appraisal_description = models.TextField(_("Appraisal Description"))
    line_no = models.PositiveIntegerField(_("Line No"))
    question = models.CharField(_("Question"), max_length=250)
    score = models.PositiveIntegerField(_("Score"))
    grading = models.CharField(_("Grading"), choices=APPRAISALGRADES.choices, max_length=50)
    answer = models.CharField(_("Answer"), max_length=250)
    comment = models.CharField(_("Comment"), max_length=250)
    scored = models.BooleanField(_("Scored"))

    class Meta:
        verbose_name = "Employee Appraisal Response"
        verbose_name_plural = "Employee Appraisal Responses"

    def __str__(self) -> str:
        return f"{self.appraisal_code}, {self.emp_code}"


class EmployeePromotion(models.Model):
    no = models.CharField(_("No."), max_length=50)
    department_code = models.ForeignKey("company.SecondCategoryLevel", verbose_name=_("Department Name"),
                                        on_delete=models.CASCADE)
    department_name = models.CharField(_("Department Name"), max_length=150)
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey("Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    paygroup = models.ForeignKey("paygroup.PayGroup", verbose_name=_("Pay Group"), on_delete=models.CASCADE)
    current_job_title_code = models.ForeignKey("company.JobTitles", verbose_name=_("Current Job"), on_delete=models.CASCADE)
    current_job_title = models.CharField(_("Current Job Title"), max_length=50, blank=True, null=True)
    new_job_title_code = models.ForeignKey("company.JobTitles", verbose_name=_("New Job Title Code"), on_delete=models.CASCADE, related_name="new_job_title_code")
    new_job_title = models.CharField(_("New Job Title"), max_length=50)
    current_salary_grade = models.ForeignKey("company.SalaryGrade", verbose_name=_("Current Salary Grade"), on_delete=models.CASCADE, related_name="current_salary_grade")
    new_salary_grade = models.ForeignKey("company.SalaryGrade", verbose_name=_("New Salary Grade"), on_delete=models.CASCADE, related_name="new_salary_grade")
    current_notch = models.PositiveIntegerField(_("Current Notch"))
    new_notch = models.PositiveIntegerField(_("New Notch"))
    current_basic_salary = models.DecimalField(_("Current Basic Salary"), max_digits=5, decimal_places=2)
    new_basic_salary = models.DecimalField(_("New Basic Salary"), max_digits=5, decimal_places=2)
    comment = models.CharField(_("Comment"), max_length=250)
    transaction_date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))
    effective_date = models.DateField(_("Effective Date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Employee Promotion"
        verbose_name_plural = "Employee Promotions"

    def __str__(self) -> str:
        return f"{self.emp_name}, {self.current_job_title}, {self.new_job_title}"


class EmployeeMedicals(models.Model):
    medical_type = models.ForeignKey("company.MedicalCodes", verbose_name=_("Medical Type"), on_delete=models.CASCADE,
                                     blank=True, null=True)
    emp_type = models.CharField(_("Employee Type"), choices=EmployeeType.choices, max_length=50)
    emp_name = models.ForeignKey("employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    department = models.ForeignKey("company.Department", verbose_name=_("Department"), on_delete=models.CASCADE)
    division_code = models.CharField(_("Division Code"), max_length=50)
    facility_code = models.CharField(_("Facility Code"), max_length=50)
    facility_name = models.CharField(_("Facility Name"), max_length=50)
    policy_code = models.CharField(_("Policy Code"), max_length=50)
    policy_description = models.CharField(_("Policy Description"), max_length=50)
    limit_type = models.CharField(_("Limit Type"), choices=MEDICALLIMITTYPE.choices, max_length=50)
    medical_limit = models.DecimalField(_("Medical Limit"), max_digits=5, decimal_places=2)
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    claim_date = models.DateField(_("Claim Date"), auto_now=False, auto_now_add=False)
    comments = models.CharField(_("Comments"), max_length=150)
    dependant = models.BooleanField(_("Dependant"))
    dependant_name = models.CharField(_("Department Name"), max_length=50)
    dependant_code = models.CharField(_("Dependant Code"), max_length=50)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Employee Medicals"
        verbose_name_plural = "Employee Medicals"

    def __str__(self) -> str:
        return f"{self.medical_type}, {self.emp_name}"


class EmployeeDisciplinaryActions(models.Model):
    emp_name = models.ForeignKey(Employee, verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    department_name = models.ForeignKey("company.Department", verbose_name=_("Department Name"),
                                        on_delete=models.CASCADE)
    division_code = models.CharField(_("Division Code"), max_length=50)
    division_name = models.CharField(_("Division Name"), max_length=50)
    disciplinary_code = models.CharField(verbose_name=_("Disciplinary Code"), max_length=50)
    description = models.CharField(_("Description"), max_length=100)
    offense_type = models.CharField(_("Offense Type"), choices=OffenseType.choices, max_length=50)
    recommended_action = models.CharField(_("Recommended Action"), choices=RecommendedAction.choices, max_length=50)
    remarks = models.CharField(_("Remarks"), max_length=250)
    suspension_start_date = models.DateField(_("Supsension Date"), blank=True, null=True, auto_now=False,
                                             auto_now_add=False)
    suspension_end_date = models.DateField(_("Suspension End Date"), blank=True, null=True, auto_now=False,
                                           auto_now_add=False)
    effective_date = models.DateField(_("Effective Date"), blank=True, null=True, auto_now=False, auto_now_add=False)
    transaction_date = models.DateField(_("Transaction Date"), blank=True, null=True, auto_now=False,
                                        auto_now_add=False)
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Employee Disciplinary Actions"
        verbose_name_plural = "Employee Disciplinary Actions"

    def __str__(self):
        return f"{self.emp_name}, {self.disciplinary_code}, {self.recommended_action}"


class EmployeePolicy(LeaveRequest):
    assignment_no = models.CharField(_("Assignment No."), max_length=50)
    last_date_modified = models.DateField(_("Last Date Modified"), auto_now=False, auto_now_add=False)
    closed = models.BooleanField(_("Closed"))

    class Meta:
        verbose_name = "Employee Policy"
        verbose_name_plural = "Employee Policies"

    def __str__(self):
        return self.assignment_no


class EmployeePayReview(models.Model):
    no = models.CharField(_("Code"), max_length=50)
    review_type = models.CharField(_("Review Type"),choices=ReviewType.choices,default=ReviewType.ANNUAL_REVIEW ,max_length=50)
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE)
    emp_name = models.CharField(_("Employee Name"), max_length=150)
    job_title_code = models.CharField(_("Job Title Code"), max_length=150)
    job_title = models.CharField(_("Job Title"), max_length=150)
    base_pay = models.DecimalField(_("BasePay"), max_digits=5, decimal_places=2)
    percentage_increase = models.DecimalField(_("Percentage Increase"), max_digits=5, decimal_places=2)
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    effective_date = models.DateField(_("Effective Date"), auto_now=True, auto_now_add=False)
    user_id = models.CharField(_("User ID"), max_length=50)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Employee Pay Review"
        verbose_name_plural = "Employee Pay Reviews"

    @property
    def new_base_pay(self):
        return round((self.base_pay + ((self.base_pay * self.percentage_increase) / 100)), 2)

    def __str__(self):
        return self.new_base_pay
