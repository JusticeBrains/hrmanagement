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


class Department(models.Model):
    name = models.CharField(_("Name Of Department"), max_length=50)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.name}"


class Holidays(models.Model):
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    holiday = models.CharField(_("Holiday"), max_length=50)

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"

    def __str__(self):
        return f"{self.holiday}, {self.date}"


class MedicalCodes(models.Model):
    description = models.CharField(_("Description"), max_length=50)
    limit_type = models.CharField(_("Limit Type"), max_length=50)
    medical_limit = models.DecimalField(
        _("Medical Limit"),
        choices=text_options.MEDICALLIMITTYPE.choices,
        max_digits=5,
        decimal_places=2,
    )
    blocked = models.BooleanField(_("Blocked"))

    class Meta:
        verbose_name = "Medical Codes"
        verbose_name_plural = "Medical Codes"

    def __str__(self):
        return self.code


class MedicalCentres(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    address = models.CharField(_("Adress"), max_length=50)
    address2 = models.CharField(_("Address2"), max_length=50, blank=True, null=True)
    contact_no = models.CharField(_("Contact Number"), max_length=50)
    contact_person = models.CharField(_("Contact Person"), max_length=50)
    blocked = models.BooleanField(_("Blocked"))

    class Meta:
        verbose_name = "Medical Centres"
        verbose_name_plural = "Medical Centres"

    def __str__(self):
        return self.name


class Property(models.Model):
    description = models.CharField(_("Description"), max_length=50)
    asset_value = models.DecimalField(_("Asset Value"), max_digits=5, decimal_places=2)
    currency = models.CharField(_("Currency"), max_length=50)
    blocked = models.BooleanField(_("Blocked"))

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.description


class DisciplinaryActions(models.Model):
    description = models.CharField(_("Description"), max_length=100)
    minor_offense = models.CharField(_("Minor Offense"), max_length=50)
    major_offense = models.CharField(_("Major Offense"), max_length=50)
    serious_offense = models.CharField(_("Serious Offense"), max_length=50)
    remarks = models.CharField(_("Remarks"), max_length=100)

    class Meta:
        verbose_name = "Disciplinary Actions"
        verbose_name_plural = "Disciplinary Actions"

    def __str__(self):
        return f"{self.description}"


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


class HRNeeds(models.Model):
    header_no = models.CharField(_("Header No."), max_length=50)
    line_no = models.PositiveIntegerField(_("Line No."))
    job_title = models.CharField(_("Job Title"), max_length=50)

    class Meta:
        abstract = True


class HRNeedsLine(HRNeeds):
    job_title_code = models.ForeignKey(
        "company.Job", verbose_name=_("Job Title Code"), on_delete=models.CASCADE
    )
    job_level_code = models.CharField(_("Job Level Code"), max_length=50)
    job_level = models.CharField(_("Job Level"), max_length=50)
    no_of_personnel_required = models.DecimalField(
        _("No. Of Personnel Required"), max_digits=5, decimal_places=2
    )

    class Meta:
        verbose_name = "HR Needs Line"
        verbose_name_plural = "HR Needs Line"

    def __str__(self):
        return self.no_of_personnel_required


class HRApprovalEntry(models.Model):
    table_id = models.CharField(_("Table ID"), max_length=50)
    document_type = models.CharField(
        _("Document Type"),
        choices=text_options.DocumentTypeOption.choices,
        max_length=50,
    )
    document_code = models.CharField(_("Document Code"), max_length=50)
    sequence_no = models.PositiveIntegerField(_("Sequence No."))
    source_code = models.CharField(_("Source Code"), max_length=50)
    sender_id = models.CharField(_("Sender ID"), max_length=50)
    approver_id = models.CharField(_("Approver ID"), max_length=50)
    status = models.CharField(
        _("Status"), choices=text_options.DocumentStatus.choices, max_length=50
    )
    date_time_sent_for_approval = models.DateField(
        _("Date Time Sent For Approval"), auto_now=True, auto_now_add=False
    )
    last_date_time_modified = models.DateTimeField(
        _("Last Modified By ID"), auto_now=True, auto_now_add=False
    )
    last_modified_by_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Last Modified By"),
        on_delete=models.CASCADE,
    )
    comment = models.CharField(_("Comment"), max_length=100)

    class Meta:
        verbose_name = "HR Approval Entry"
        verbose_name_plural = "HR Approval Entries"

    def __str__(self):
        pass


class HRAlerts(models.Model):
    entry_no = models.PositiveIntegerField(_("Entry No."))
    emp_code = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE
    )
    alert_type = models.CharField(
        _("Alert Type"), choices=text_options.DocumentTypeOption.choices, max_length=50
    )
    description = models.CharField(_("Description"), max_length=200)
    alert_date = models.DateField(_("Alert Date"), auto_now=True, auto_now_add=False)
    dismissed = models.BooleanField(_("Dismissed"))
    date_dismissed = models.DateField(
        _("Date Dismissed"), auto_now=True, auto_now_add=False
    )
    user_id = models.CharField(_("User ID"), max_length=50)


class Meta:
    verbose_name = "HR Alerts"
    verbose_name_plural = "HR Alerts"


class WorkmenCompensation(models.Model):
    no = models.CharField(_("No."), max_length=50)
    type = models.CharField(
        _("Type"), choices=text_options.WorkmenOption.choices, max_length=50
    )
    emp_code = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE
    )
    emp_name = models.CharField(_("Employee Name"), max_length=150)
    job_title_code = models.CharField(_("Job Title"), max_length=50)
    job_title = models.ForeignKey(
        "Job", verbose_name=_("Job Title"), on_delete=models.CASCADE
    )
    division = models.CharField(_("Division"), max_length=50)
    department = models.ForeignKey(
        "Department", verbose_name=_("Department"), on_delete=models.CASCADE
    )
    incident_details = models.CharField(_("Incident Details"), max_length=50)
    nature_of_injury = models.CharField(_("Nature Of Injury"), max_length=100)
    incident_date = models.DateField(
        _("Incident Date"), auto_now=True, auto_now_add=False
    )
    amount_paid = models.DecimalField(_("Amount Paid"), max_digits=5, decimal_places=2)
    percentage_awarded = models.DecimalField(
        _("Percentage Awarded"), max_digits=5, decimal_places=2
    )
    compensation_date = models.DateField(
        _("Compensation Date"), auto_now=True, auto_now_add=False
    )
    name_of_issuer = models.CharField(_("Name Of Issuer"), max_length=50)
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Workmen Compensation"
        verbose_name_plural = "Workmen Compensations"

    def str(self):
        return self.amount_paid


class Expatriates(models.Model):
    company_code = models.ForeignKey(
        "company.Company", verbose_name=_("Company Code"), on_delete=models.CASCADE
    )
    expatriate_no = models.CharField(_("Expatraited No"), max_length=50)
    name = models.CharField(_("Name"), max_length=150)
    gender = models.CharField(
        _("Gender"), choices=text_options.GENDER.choices, max_length=50
    )
    nationality = models.CharField(_("Nationality"), max_length=50)
    passport_page = models.BooleanField(_("Passport Page"))
    curriculum_vitae = models.BooleanField(_("Curriculium Vitae"))
    medical_report = models.BooleanField(_("Medical Report"))
    employment_contract = models.BooleanField(_("Employment Contract"))
    police_report = models.BooleanField(_("Police Report"))
    passport_no = models.CharField(_("Passport No"), max_length=50)
    place_of_issue = models.CharField(_("Place Of Issue"), max_length=50)
    date_of_issue = models.DateField(
        _("Date Of Issue"), auto_now=True, auto_now_add=False
    )
    job_code = models.ForeignKey(
        "Job", verbose_name=_("Job Code"), on_delete=models.CASCADE
    )
    contract_no = models.CharField(_("Contract No."), max_length=50)
    party1 = models.CharField(_("Party 1"), max_length=150)
    party2 = models.CharField(_("Party 2"), max_length=150)
    purpose_of_contract = models.CharField(_("Purpose Of Contract"), max_length=200)
    duration_of_contract = models.PositiveIntegerField(
        _("Duration Of Contract(Months)")
    )
    commencement_date = models.DateField(
        _("Commencement Date"), auto_now=True, auto_now_add=False
    )

    class Meta:
        verbose_name = "Expatriates"
        verbose_name_plural = "Expatriates"

    def __str__(self):
        return self.expatriate_no


class ExpatriateApplication(models.Model):
    expatriate_no = models.CharField(_("Expatriate No."), max_length=50)
    application_no = models.PositiveIntegerField(_("Application No."))
    date_of_application = models.DateField(
        _("Date Of Application"), auto_now=True, auto_now_add=False
    )
    date_received = models.DateField(
        _("Date Received"), auto_now=True, auto_now_add=False
    )
    date_of_expatriate_arrival = models.DateField(
        _("Date Of Expatriate Arrival"), auto_now=True, auto_now_add=False
    )
    duration_of_stay = models.PositiveIntegerField(_("Duration Of Stay(Months)"))
    date_of_submission = models.DateField(
        _("Date Of Submission"), auto_now=True, auto_now_add=False
    )
    date_of_approval = models.DateField(
        _("Date Of Approval"), auto_now=True, auto_now_add=False
    )
    interior_ref_number = models.CharField(_("Interior Ref No."), max_length=50)
    comments = models.CharField(_("Comments"), max_length=100)
    application_to_gnpc = models.BooleanField(_("Application To GNPC"))
    application_to_ministry = models.BooleanField(_("Application TO Ministry"))

    class Meta:
        verbose_name = "Expatriate Application"
        verbose_name_plural = "Expatriate Application"

    def __str__(self):
        return self.application_no


class CompanyStaffBreakdown(models.Model):
    company_code = models.CharField(_("Company Code"), max_length=50)
    field_code = models.CharField(_("Field Code"), max_length=50)
    employee_type = models.CharField(
        _("Employee Type"),
        choices=text_options.CompanyEmployeeType.choices,
        max_length=150,
    )
    fieldname = models.CharField(_("Field Name"), max_length=50)
    management = models.PositiveIntegerField(_("Management"))
    senior_staff = models.PositiveIntegerField(_("Senior Staff"))
    junior_staff = models.PositiveIntegerField(_("Junior Staff"))
    other_staff = models.PositiveIntegerField(_("Other Staff"))
    total = models.PositiveIntegerField(_("Total"))
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    current = models.BooleanField(_("Current"))

    class Meta:
        verbose_name = "Company Staff Breakdown"
        verbose_name_plural = "Company Staff Breakdowns"

    def __str__(self):
        return self.employee_type


class PassportIssues(models.Model):
    entry_no = models.PositiveIntegerField(_("Entry No."))
    emp_code = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE
    )
    emp_name = models.CharField(_("Employee Name"), max_length=150)
    passport_no = models.CharField(_("Passport No"), max_length=50)
    date_of_issue = models.DateField(
        _("Date Of Issue"), auto_now=True, auto_now_add=False
    )
    date_of_expiry = models.DateField(
        _("Date Of Expiry"), auto_now=True, auto_now_add=False
    )
    visa_type = models.CharField(
        _("Visa Type"), choices=text_options.VisaType.choices, max_length=50
    )
    country = models.CharField(_("Country"), max_length=50)
    travel_date = models.DateField(_("Travel Date"), auto_now=True, auto_now_add=False)
    return_date = models.DateField(_("Return Date"), auto_now=True, auto_now_add=False)
    purpose_of_trip = models.CharField(_("Purpose Of Trip"), max_length=50)
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Passport Issues"
        verbose_name_plural = "Passport Issues"

    def __str__(self):
        return f"{self.visa_type}, {self.emp_name}"

    @property
    def duration(self):
        return self.date_of_expiry - self.date_of_issue


class PerformanceOverview(models.Model):
    type = models.CharField(
        _("Type"), choices=text_options.PerformanceOverviewType.choices, max_length=50
    )
    no = models.CharField(_("No."), max_length=50)
    emp_code = models.CharField(_("Employee Name"), max_length=50)
    emp_name = models.CharField(_("Employee Name"), max_length=150)
    supervisor_name = models.CharField(_("Supervisor Name"), max_length=150)
    next_supervisor_name = models.CharField(_("Next Supervisor"), max_length=150)
    entry_date = models.DateField(_("Entry Date"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Performance Overview"
        verbose_name_plural = "Performance Overview"

    def __str__(self):
        return self.type


class OrganizationalStructure(models.Model):
    department_code = models.ForeignKey(
        "company.Department",
        verbose_name=_("Department Code"),
        on_delete=models.CASCADE,
    )
    organizational_level_code = models.CharField(
        _("Organizational Level Code"), max_length=50
    )
    level_description = models.CharField(_("Level Description"), max_length=50)
    reports_to_level = models.CharField(_("Reports To Level"), max_length=50)
    level_in_structure = models.PositiveIntegerField(_("Level In Structure"))

    class Meta:
        verbose_name = "Organizational Structure"
        verbose_name_plural = "Organizational Structure"

    def __str__(self):
        return self.organizational_level_code


class GrievanceHeader(models.Model):
    no = models.CharField(_("No."), max_length=50)
    review_type = models.CharField(
        _("Review Type"), choices=text_options.ReviewType.choices, max_length=50
    )
    year_of_review = models.PositiveIntegerField(_("Year Of Review"))
    review_no = models.CharField(_("Review No."), max_length=50)
    department_code = models.ForeignKey(
        "company.Department",
        verbose_name=_("Department Code"),
        on_delete=models.CASCADE,
    )
    department_name = models.CharField(_("Department Name"), max_length=50)
    emp_code = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE
    )
    job_title = models.CharField(_("Job Title"), max_length=50)
    employment_date = models.DateField(
        _("Employment Date"), auto_now=True, auto_now_add=False
    )
    supervisor_level = models.CharField(_("Supervisor Level"), max_length=150)
    supervisor_name = models.CharField(_("Supervisor Name"), max_length=150)
    supervisor_job_title = models.CharField(_("Supervisor Job Title"), max_length=50)
    next_supervisor_level = models.CharField(_("Supervisor Level"), max_length=150)
    next_supervisor_name = models.CharField(_("Next Supervisor Name"), max_length=150)
    next_supervisor_job_title = models.CharField(
        _("Next Supervisor Job Title"), max_length=50
    )
    next_supervisor_signed = models.BooleanField(_("Employee Signed"))
    next_supervisor_signed_date = models.DateField(
        _("Employee Signed Date"), auto_now=True, auto_now_add=False
    )
    grievance_description = models.CharField(
        _("Grieveance Description"), max_length=250
    )
    grievance_date = models.DateField(
        _("Grievance Date"), auto_now=True, auto_now_add=False
    )
    grievance_posted = models.BooleanField(_("Grievance POsted"))
    supervisor_respond = models.CharField(_("Supervisor Respond"), max_length=250)
    supervisor_respond_date = models.DateField(
        _("Supervisor Respond Date"), auto_now=True, auto_now_add=False
    )
    response_posted = models.BooleanField(_("Response Posted"))
    next_supervisor_respond = models.CharField(
        _("Next Supervisor Respond"), max_length=250
    )
    next_supervisor_respond_date = models.DateField(
        _("Next Supervisor Respond Date"), auto_now=True, auto_now_add=False
    )
    next_response_posted = models.BooleanField(_("Next Response Posted"))
    transation_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.CharField(_("User ID"), max_length=50)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Grievance Header"
        verbose_name_plural = "Grievance Headers"

    def __str__(self):
        return self.no


class GrievanceLine(models.Model):
    header_no = models.ForeignKey(
        "GrievanceHeader", verbose_name=_("Header No."), on_delete=models.CASCADE
    )
    entry_no = models.PositiveIntegerField(_("Entry No."))
    performance_target = models.CharField(_("Performance Target"), max_length=250)
    corporate_objective_code = models.CharField(
        _("Corporate Objective Code"), max_length=50
    )
    dept_objective_entry_no = models.PositiveIntegerField(
        _("Departmental Objective Entry No.")
    )
    departmental_objective_text = models.CharField(
        _("Departmental Objective Text"), max_length=150
    )
    measurement_indicator = models.CharField(_("Measurement Indicator"), max_length=250)
    weight = models.DecimalField(_("Weight"), max_digits=5, decimal_places=2)
    target_date = models.DateField(_("Target Date"), auto_now=True, auto_now_add=False)
    rating = models.PositiveIntegerField(_("Rating"))
    rating_result = models.CharField(
        _("Rating Result"), choices=text_options.RatingResult.choices, max_length=50
    )
    remarks = models.CharField(_("Remarks"), max_length=250)
    achievements = models.CharField(_("Achievements"), max_length=250)
    grievance = models.CharField(_("Grievance"), max_length=250)
    supervisor_response = models.CharField(_("Supervisor Response"), max_length=250)
    next_supervisor_response = models.CharField(
        _("Next Supervisor Response"), max_length=250
    )

    class Meta:
        verbose_name = "Grievance Line"
        verbose_name_plural = "Grievance Lines"

    def __str__(self):
        return self.grievance


class GrievanceEntry(models.Model):
    no = models.CharField(_("No."), max_length=50)
    employee_code = models.CharField(_("Employee Code"), max_length=50)
    employee_name = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE
    )
    department_code = models.CharField(_("Department Code"), max_length=50)
    department_name = models.ForeignKey(
        "company.Department",
        verbose_name=_("Department Name"),
        on_delete=models.CASCADE,
    )
    job_title_code = models.CharField(_("Job Title Code"), max_length=50)
    job_title = models.CharField(_("Job Title"), max_length=150)
    nature_of_grievance = models.CharField(_("Nature Of Grievance"), max_length=50)
    status = models.CharField(_("Status"), max_length=50)
    decision_taken = models.CharField(_("Decision Taken"), max_length=100)
    effective_date = models.DateField(
        _("Effective Date"), auto_now=True, auto_now_add=False
    )
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.ForeignKey(
        User, verbose_name=_("User ID"), on_delete=models.CASCADE
    )
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Grievance Entry"
        verbose_name_plural = "Grievance Entries"

    def __str__(self):
        return self.no


class GrievanceCommitteMembers(models.Model):
    grievance_code = models.CharField(_("Grievance Code"), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No"))
    member_name = models.CharField(_("Member Name"), max_length=150)
    address = models.CharField(_("Address"), max_length=50)
    phone_no = models.CharField(_("Phone No."), max_length=20)

    class Meta:
        verbose_name = "Grievance Committe Members"
        verbose_name_plural = "Grievance Committe Members"

    def __str__(self):
        return self.member_name


class Travels(models.Model):
    no = models.CharField(_("No."), max_length=50)
    personnel_type = models.CharField(
        _("Personnel Type"), choices=text_options.PersonnelType.choices, max_length=50
    )
    employee_no = models.CharField(_("Employee No"), max_length=50)
    personnel_name = models.CharField(_("Personnel Name"), max_length=100)
    travel_start_date = models.DateField(
        _("Travel Start Date"), auto_now=True, auto_now_add=False
    )
    travel_end_date = models.DateField(
        _("Travel End Date"), auto_now=True, auto_now_add=False
    )
    destination = models.CharField(_("Destination"), max_length=100)
    purpose = models.CharField(_("Purpose"), max_length=250)
    contact_person = models.CharField(_("Contact Person"), max_length=150)
    contact_phone_no = models.CharField(_("Contact Phone No."), max_length=50)
    currency_code = models.CharField(_("Curremt Code"), max_length=50)
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.ForeignKey(
        User, verbose_name=_("User ID"), on_delete=models.CASCADE
    )
    posted = models.BooleanField(_("Posted"))
    total_expense = models.DecimalField(
        _("Total Expense"), max_digits=5, decimal_places=2
    )

    class Meta:
        verbose_name = "Travels"
        verbose_name_plural = "Travels"


class TravelExpenses(models.Model):
    travel_no = models.ForeignKey(
        "company.Travels", verbose_name=_("Travel No"), on_delete=models.CASCADE
    )
    expense_code = models.CharField(_("Expense Code"), max_length=50)
    expense_description = models.TextField(_("Expense Description"))
    currency_code = models.CharField(_("Currency Code"), max_length=50)
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Travel Expenses"
        verbose_name_plural = "Travel Expenses"


class CourierCompanies(models.Model):
    entry_no = models.PositiveIntegerField(_("Entry No."))
    company_name = models.CharField(_("Company Name"), max_length=50)
    contact_person = models.CharField(_("Contact Person"), max_length=50)
    contact_person_no = models.CharField(_("Contact Person's No."), max_length=50)
    office_location = models.CharField(_("Office Location"), max_length=50)
    comments = models.TextField(_("Commments"))

    class Meta:
        verbose_name = "Courier Companies"
        verbose_name_plural = "Courier Companies"


class CourierServiceRequisition(models.Model):
    no = models.CharField(_("No."), max_length=50)
    requesting_dept_code = models.CharField(
        _("Requesting Department Code"), max_length=50
    )
    requesting_department = models.ForeignKey(
        "company.Department",
        verbose_name=_("Requesting Department"),
        on_delete=models.CASCADE,
    )
    requesting_officer = models.CharField(_("Requesting Officer"), max_length=150)
    destination_address = models.CharField(_("Destination Address"), max_length=100)
    parcel_type = models.CharField(_("Parcel Type"), max_length=100)
    serial_no = models.CharField(_("Serial No."), max_length=50)
    date_of_delivery_to_courier = models.DateField(
        _("Date Of Delivery To Courier"), auto_now=True, auto_now_add=False
    )
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.ForeignKey(
        User, verbose_name=_("User ID"), on_delete=models.CASCADE
    )
    courier_no = models.PositiveIntegerField(_("Courier No."))
    courier_service_operator = models.CharField(
        _("Courier Service Operator"), max_length=50
    )
    document_serial_no = models.CharField(_("Document Serial No"), max_length=50)
    billing_amount = models.DecimalField(
        _("Billing Amount"), max_digits=5, decimal_places=2
    )
    posted = models.BooleanField(_("Posted"))
    billed = models.BooleanField(_("Billed"))

    class Meta:
        verbose_name = "Courier Service Requistition"
        verbose_name_plural = "Courier Service Requistitions"


class HospitalityFacilities(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = "Hospitality Facilities"
        verbose_name_plural = "Hospitality Facilities"


class HospitalityServices(models.Model):
    no = models.CharField(_("No."), max_length=50)
    hospitality_facility_code = models.CharField(
        _("Hospitality Facility Code"), max_length=50
    )
    hospitality_facility = models.ForeignKey(
        "company.HospitalityFacilities", verbose_name=_(""), on_delete=models.CASCADE
    )
    services_provided = models.TextField(_("Services Provided"))
    location = models.TextField(_("Location"))
    date_of_transaction = models.DateField(
        _("Date Of TRansaction"), auto_now=True, auto_now_add=False
    )
    bill_amount = models.DecimalField(_("Bill Amount"), max_digits=5, decimal_places=2)
    comments = models.TextField(_("Comments"))
    user_id = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Hospitality Services"
        verbose_name_plural = "Hospitality Services"


class CollectiveBargaining(models.Model):
    no = models.CharField(_("No."), max_length=50)
    description = models.TextField(_("Description"))
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=True, auto_now_add=False)
    status = models.CharField(_("Status"), max_length=50)
    date_of_new_cba = models.DateField(
        _("Date Of New CBA"), auto_now=True, auto_now_add=False
    )
    expiry_date = models.DateField(_("Expiry Date"), auto_now=True, auto_now_add=False)
    transaction_date = models.DateField(
        _("Transaction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.ForeignKey(
        User, verbose_name=_("User ID"), on_delete=models.CASCADE
    )
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Collective Bargaining"
        verbose_name_plural = "Collective Bargaining"


class CBASJNC(models.Model):
    cba_no = models.CharField(_("CBA No."), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No."))

    class Meta:
        abstract = True


class CBAIssues(CBASJNC):
    issues_negotiated = models.TextField(_("Issues Negotiated"))
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    status = models.TextField(_("Status"))

    class Meta:
        verbose_name = "CBA Issues"
        verbose_name_plural = "CBA Issues"


class SJNCMembers(CBASJNC):
    employee_code = models.CharField(_("Employee Code"), max_length=50)
    member_name = models.CharField(_("Memeber Name"), max_length=150)

    class Meta:
        verbose_name = "SJNC Members"
        verbose_name_plural = "SJNC Members"


class CashService(models.Model):
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey(
        "employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE
    )
    department_code = models.CharField(_("Department Code"), max_length=50)
    department_name = models.ForeignKey(
        "company.Department",
        verbose_name=_("Department Code"),
        on_delete=models.CASCADE,
    )
    job_title_code = models.CharField(_("Job Title Code"), max_length=50)
    job_title = models.ForeignKey(
        "company.Job", verbose_name=_("Job Title"), on_delete=models.CASCADE
    )
    base_pay = models.DecimalField(_("Base Pay"), max_digits=5, decimal_places=2)
    transaction_date = models.DateField(
        _("Transaxction Date"), auto_now=True, auto_now_add=False
    )
    user_id = models.ForeignKey(
        User, verbose_name=_("User ID"), on_delete=models.CASCADE
    )
    posted = models.BooleanField(_("Posted"))

    class Meta:
        abstract = True


class CashBenefitPayments(CashService):
    entry_no = models.PositiveIntegerField(_("Entry No."))
    payment_type = models.CharField(_("Payment Type"), max_length=50)
    date_of_seperation = models.DateField(
        _("Date Of Seperation"), auto_now=True, auto_now_add=False
    )
    amount_paid = models.DecimalField(_("Amount Paid"), max_digits=5, decimal_places=2)
    date_paid = models.DateField(_("Date Paid"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Cash Benefit Payments"
        verbose_name_plural = "Cash Benefit Payments"


class EndOfServiceEntry(CashService):
    no = models.CharField(_("No."), max_length=50)
    type = models.CharField(
        _("Type"), choices=text_options.EndOfServiceOptions.choices, max_length=50
    )
    employment_date = models.DateField(
        _("Employment Date"), auto_now=True, auto_now_add=False
    )
    end_of_service_date = models.DateField(
        _("End Of Service Date"), auto_now=True, auto_now_add=False
    )
    no_of_years_service = models.PositiveIntegerField(_("No. Of Years Service"))
    no_of_excess_months_service = models.PositiveIntegerField(
        _("No. Of Excess Months Service")
    )
    no_of_months_pay = models.DecimalField(
        _("No. Of Months Pay"), max_digits=5, decimal_places=2
    )
    total_esb_amount = models.DecimalField(
        _("Total ESB Amount"), max_digits=5, decimal_places=2
    )
    add_on_amount = models.DecimalField(
        _("Add On Amount"), max_digits=5, decimal_places=2
    )
    final_total = models.DecimalField(_("Final Total"), max_digits=5, decimal_places=2)
    award_received = models.TextField(_("Award Received"))

    class Meta:
        verbose_name = "End Of Service Entry"
        verbose_name_plural = "End Of Service Entries"

    @property
    def service_duration(self):
        return self.end_of_service_date - self.employment_date


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
