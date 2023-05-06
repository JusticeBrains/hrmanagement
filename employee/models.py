
import uuid
from options.text_options import (
    GENDER,
    EMPLOYEESTATUS,
    MARITALSTATUS,
    APPRAISALGRADES,
    ReviewType,
    EmployeeType,
    MEDICALLIMITTYPE,
    OffenseType,
    RecommendedAction,
)
from django.db import connection
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()


class Employee(models.Model):
    code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    initials = models.CharField(_("Initials"), max_length=40, blank=True, null=True)
    search_name = models.CharField(
        _("Search Name"), max_length=50, blank=True, null=True
    )
    gender = models.CharField(_("Gender"), max_length=50, blank=True, null=True)
    phone_no2 = models.CharField(
        _("Phone Number 2"), max_length=50, blank=True, null=True
    )
    company_email = models.EmailField(
        _("Company Email"), max_length=254, blank=True, null=True
    )
    job_titles = models.CharField(_("Job Titles"), max_length=50, blank=True, null=True)
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
    first_category_level = models.CharField(
        _("First Category Level"), max_length=250, blank=True, null=True
    )
    second_category_level = models.CharField(
        _("Second Category Level"), max_length=250, blank=True, null=True
    )
    third_category_level = models.CharField(
        _("Third Category Level"), max_length=250, blank=True, null=True
    )
    fourth_category_level = models.CharField(
        _("Fourth Category Level"), max_length=250, blank=True, null=True
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
    statistics_group_code = models.CharField(
        _("Statistics Group Code"), max_length=250, null=True, blank=True
    )
    resource_no = models.CharField(
        _("Resource No"), max_length=250, blank=True, null=True
    )
    salesperson_purch_code = models.CharField(
        _("Salespers Purch Code"), max_length=250, null=True, blank=True
    )
    birth_date = models.CharField(_("Birth Date"), max_length=50, blank=True, null=True)
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
    pay_group_code = models.CharField(
        _("Pay Group Code"), max_length=50, blank=True, null=True
    )
    salary_grade = models.CharField(
        _("Salary Grade"), max_length=50, blank=True, null=True
    )
    notch = models.CharField(_("Notch"), max_length=50, blank=True, null=True)
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
    bank_code = models.CharField(_("Bank Code"), max_length=50, blank=True, null=True)
    bank_name = models.CharField(_("Bank Name"), max_length=50, blank=True, null=True)
    bank_branch_code = models.CharField(
        _("Bank Branch Code"), max_length=50, blank=True, null=True
    )
    bank_branch_name = models.CharField(
        _("Bank Branch Name"), max_length=50, blank=True, null=True
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
    staff_category_code = models.ForeignKey(
        "employee.StaffCategory",
        verbose_name=_("Staff Category"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    days_left = models.PositiveIntegerField(_("Days Left"), null=True, blank=True, default=0)
    no_of_days_exhausted = models.PositiveIntegerField(_("No. Of Days Exhausted"), blank=True, null=True)
    plan_days_left = models.PositiveIntegerField(_("Plan Days Left"), null=True, blank=True, default=0)
    plan_no_of_days_exhausted = models.PositiveIntegerField(_("Plan No. Of Days Exhausted"), blank=True, null=True)


    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
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


class AppraisalAreas(models.Model):
    description = models.CharField(_("Description"), max_length=50)
    scored = models.BooleanField(_("Scored"))

    class Meta:
        verbose_name = "Appraisal Areas"
        verbose_name_plural = "Appraisal Areas"


class EmployeeAppraisal(models.Model):
    emp_code = models.ForeignKey(
        Employee,
        verbose_name=_("Employee Code"),
        on_delete=models.CASCADE,
        related_name="emp_code",
    )
    emp_name = models.CharField(verbose_name=_("Employee Name"), max_length=50)
    paygroup_code = models.ForeignKey(
        "paygroup.PayGroup",
        verbose_name=_("Pay Groups"),
        on_delete=models.CASCADE,
        related_name="paygroup_code",
    )
    job_title_code = models.ForeignKey(
        "company.JobTitles",
        verbose_name=_("Job Title"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    job_title = models.CharField(_("Job Title"), max_length=150)
    appraisal_date = models.DateField(
        _("Appraisal Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    appraisal_venue = models.CharField(
        _("Appraisal Venue"), max_length=50, blank=True, null=True
    )
    appraiser = models.CharField(
        verbose_name="Appraiser", max_length=200, blank=True, null=True
    )
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"), blank=True, null=True)

    class Meta:
        verbose_name = "Employee Appraisal"
        verbose_name_plural = "Employee Appraisals"


class EmployeeAppraisalResponse(models.Model):
    appraisal_no = models.CharField(_("Appraisal No."), max_length=50)
    emp_code = models.CharField(verbose_name=_("Employee"), max_length=50)
    appraisal_code = models.CharField(
        verbose_name=_("Employee Appraisal Code"), max_length=50
    )
    appraisal_description = models.TextField(_("Appraisal Description"))
    line_no = models.PositiveIntegerField(_("Line No"))
    question = models.CharField(_("Question"), max_length=250)
    score = models.PositiveIntegerField(_("Score"))
    grading = models.CharField(
        _("Grading"), choices=APPRAISALGRADES.choices, max_length=50
    )
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
    department_code = models.ForeignKey(
        "company.SecondCategoryLevel",
        verbose_name=_("Department Name"),
        on_delete=models.CASCADE,
    )
    department_name = models.CharField(_("Department Name"), max_length=150)
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey(
        "Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE
    )
    paygroup = models.ForeignKey(
        "paygroup.PayGroup", verbose_name=_("Pay Group"), on_delete=models.CASCADE
    )
    current_job_title_code = models.ForeignKey(
        "company.JobTitles", verbose_name=_("Current Job"), on_delete=models.CASCADE
    )
    current_job_title = models.CharField(
        _("Current Job Title"), max_length=50, blank=True, null=True
    )
    new_job_title_code = models.ForeignKey(
        "company.JobTitles",
        verbose_name=_("New Job Title Code"),
        on_delete=models.CASCADE,
        related_name="new_job_title_code",
    )
    new_job_title = models.CharField(_("New Job Title"), max_length=50)
    current_salary_grade = models.ForeignKey(
        "company.SalaryGrade",
        verbose_name=_("Current Salary Grade"),
        on_delete=models.CASCADE,
        related_name="current_salary_grade",
    )
    new_salary_grade = models.ForeignKey(
        "company.SalaryGrade",
        verbose_name=_("New Salary Grade"),
        on_delete=models.CASCADE,
        related_name="new_salary_grade",
    )
    current_notch = models.PositiveIntegerField(_("Current Notch"))
    new_notch = models.PositiveIntegerField(_("New Notch"))
    current_basic_salary = models.DecimalField(
        _("Current Basic Salary"), max_digits=5, decimal_places=2
    )
    new_basic_salary = models.DecimalField(
        _("New Basic Salary"), max_digits=5, decimal_places=2
    )
    comment = models.CharField(_("Comment"), max_length=250)
    transaction_date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))
    effective_date = models.DateField(
        _("Effective Date"), auto_now=False, auto_now_add=False
    )

    class Meta:
        verbose_name = "Employee Promotion"
        verbose_name_plural = "Employee Promotions"

    def __str__(self) -> str:
        return f"{self.emp_name}, {self.current_job_title}, {self.new_job_title}"


class EmployeeMedicals(models.Model):
    medical_type = models.ForeignKey(
        "company.MedicalCodes",
        verbose_name=_("Medical Type"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    emp_type = models.CharField(
        _("Employee Type"), choices=EmployeeType.choices, max_length=50
    )
    emp_name = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        "company.Department", verbose_name=_("Department"), on_delete=models.CASCADE
    )
    division_code = models.CharField(_("Division Code"), max_length=50)
    facility_code = models.CharField(_("Facility Code"), max_length=50)
    facility_name = models.CharField(_("Facility Name"), max_length=50)
    policy_code = models.CharField(_("Policy Code"), max_length=50)
    policy_description = models.CharField(_("Policy Description"), max_length=50)
    limit_type = models.CharField(
        _("Limit Type"), choices=MEDICALLIMITTYPE.choices, max_length=50
    )
    medical_limit = models.DecimalField(
        _("Medical Limit"), max_digits=5, decimal_places=2
    )
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    claim_date = models.DateField(_("Claim Date"), auto_now=False, auto_now_add=False)
    comments = models.CharField(_("Comments"), max_length=150)
    dependant = models.BooleanField(_("Dependant"))
    dependant_name = models.CharField(_("Department Name"), max_length=50)
    dependant_code = models.CharField(_("Dependant Code"), max_length=50)
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=False, auto_now_add=False
    )
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Employee Medicals"
        verbose_name_plural = "Employee Medicals"

    def __str__(self) -> str:
        return f"{self.medical_type}, {self.emp_name}"


class EmployeeDisciplinaryActions(models.Model):
    emp_name = models.ForeignKey(
        Employee, verbose_name=_("Employee Name"), on_delete=models.CASCADE
    )
    department_name = models.ForeignKey(
        "company.Department",
        verbose_name=_("Department Name"),
        on_delete=models.CASCADE,
    )
    division_code = models.CharField(_("Division Code"), max_length=50)
    division_name = models.CharField(_("Division Name"), max_length=50)
    disciplinary_code = models.CharField(
        verbose_name=_("Disciplinary Code"), max_length=50
    )
    description = models.CharField(_("Description"), max_length=100)
    offense_type = models.CharField(
        _("Offense Type"), choices=OffenseType.choices, max_length=50
    )
    recommended_action = models.CharField(
        _("Recommended Action"), choices=RecommendedAction.choices, max_length=50
    )
    remarks = models.CharField(_("Remarks"), max_length=250)
    suspension_start_date = models.DateField(
        _("Supsension Date"), blank=True, null=True, auto_now=False, auto_now_add=False
    )
    suspension_end_date = models.DateField(
        _("Suspension End Date"),
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False,
    )
    effective_date = models.DateField(
        _("Effective Date"), blank=True, null=True, auto_now=False, auto_now_add=False
    )
    transaction_date = models.DateField(
        _("Transaction Date"), blank=True, null=True, auto_now=False, auto_now_add=False
    )
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Employee Disciplinary Actions"
        verbose_name_plural = "Employee Disciplinary Actions"

    def __str__(self):
        return f"{self.emp_name}, {self.disciplinary_code}, {self.recommended_action}"



class EmployeePayReview(models.Model):
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
    user_id = models.CharField(_("User ID"), max_length=50)
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
    # id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=50, unique=True, primary_key=True)
    name = models.CharField(_("Name"), max_length=150, blank=True, null=True)

    class Meta:
        abstract = True


class StaffCategory(Base):
    max_number_of_days = models.PositiveIntegerField(_("Max Number Of Days"))

    class Meta:
        verbose_name = "Staff Category"
        verbose_name_plural = "Staff Categories"

    def __str__(self):
        return f"{self.code} - {self.name} - {self.max_number_of_days}"

# Set the data type of the primary key to VARCHAR in PostgreSQL
if connection.vendor == 'postgresql':
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS(
                SELECT * FROM information_schema.columns
                WHERE table_name = 'employee_staffcategory' AND column_name = 'code'
            )
        """)
        column_exists = cursor.fetchone()[0]
        if column_exists:
            cursor.execute("ALTER TABLE employee_staffcategory ALTER COLUMN code TYPE VARCHAR(50)")



class Department(Base):
    first_category_code = models.CharField(
        _("First Category Code"), max_length=50, blank=True, null=True
    )

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.code} - {self.first_category_code}"
    

if connection.vendor == 'postgresql':
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS(
                SELECT * FROM information_schema.columns
                WHERE table_name = 'employee_department' AND column_name = 'code'
            )
        """)
        column_exists = cursor.fetchone()[0]
        if column_exists:
            cursor.execute("ALTER TABLE employee_department ALTER COLUMN code TYPE VARCHAR(50)")


class Unit(Base):
    second_category_code = models.CharField(
        _("Second Category Code"), max_length=50, blank=True, null=True
    )

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"

    def __str__(self):
        return f"{self.code} - {self.second_category_code}"


if connection.vendor == 'postgresql':
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS(
                SELECT * FROM information_schema.columns
                WHERE table_name = 'employee_unit' AND column_name = 'code'
            )
        """)
        column_exists = cursor.fetchone()[0]
        if column_exists:
            cursor.execute("ALTER TABLE employee_unit ALTER COLUMN code TYPE VARCHAR(50)")



class Branch(Base):
    third_category_code = models.CharField(
        _("Third Category Code"), max_length=50, blank=True, null=True
    )

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return f"{self.code} - {self.third_category_code}"

# # Set the data type of the primary key to VARCHAR in PostgreSQL
if connection.vendor == 'postgresql':
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS(
                SELECT * FROM information_schema.columns
                WHERE table_name = 'employee_branch' AND column_name = 'code'
            )
        """)
        column_exists = cursor.fetchone()[0]
        if column_exists:
            cursor.execute("ALTER TABLE employee_branch ALTER COLUMN code TYPE VARCHAR(50)")

class Notch(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    payroll_structure_code = models.CharField(_("Payroll Structure Code"), max_length=50,blank=True, null=True)
    salary_grade = models.CharField(_("Salary Grade"), max_length=50, null=True, blank=True)
    no = models.CharField(_("No"), max_length=50, blank=True, null=True)
    amount = models.DecimalField(_("Amount"), max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.payroll_structure_code} - {self.salary_grade} - {self.no} - {self.amount}"
    
    class Meta:
        verbose_name = "Notch"
        verbose_name_plural = "Notches"


class PayCategoryList(models.Model):
    no = models.CharField(_("No"), max_length=50, blank=True, null=True)
    description = models.CharField(_("Description"), max_length=50, blank=True, null=True)
    taxable_income_code = models.CharField(_("Taxable Income Code"), max_length=50, blank=True, null=True)
    taxable_income_description = models.CharField(_("Taxable Income Description"), max_length=50, blank=True, null=True)
    tax_code = models.CharField(_("Tax Code"), max_length=50, blank=True, null=True)
    tax_description = models.CharField(_("Tax Description"), max_length=50, blank=True, null=True)
    gross_income_code = models.CharField(_("Gross Income Code"), max_length=50, blank=True, null=True)
    gross_income_description = models.CharField(_("Gross Income Description"), max_length=50, blank=True, null=True)
    bonus_tax_code = models.CharField(_("Bonus Tax Code"), max_length=50, blank=True, null=True)
    bonus_tax_description = models.CharField(_("Bonus Tax Description"), max_length=50, blank=True, null=True)
    currency_code = models.CharField(_("Currency Code"), max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.no} - {self.description} - {self.taxable_income_code}"
    
    class Meta:
        verbose_name = "Pay Category List"
        verbose_name_plural = "Pay Category Lists"