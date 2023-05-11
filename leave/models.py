from django.db import connection, models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime, timedelta, date
from employee.models import Employee
from django.utils import timezone

from options import text_options
from django.utils import timezone

User = get_user_model()


class HolidayCalender(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=80)
    holiday_date = models.DateField(_("Holiday Date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Holiday Calender"
        verbose_name_plural = "Holiday Calenders"
    
    def __str__(self):
        return f"{self.name} - {self.holiday_date}"


class LeaveBase(models.Model):
    leave_type = models.ForeignKey(
        "leave.LeaveType",
        verbose_name=_("Leave Type"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    start_date = models.DateField(_("Start Date"), default=timezone.now)
    no_of_days_requested = models.PositiveIntegerField(_("No Of Days Requested"))
    job_description = models.CharField(
        _("Job Description"), max_length=150, null=True, blank=True
    )
    job_title = models.CharField(_("Job Title"), max_length=50, null=True, blank=True)
    employee_unit = models.CharField(
        _("Employee Unit"), max_length=80, null=True, blank=True
    )
    employee_branch = models.CharField(
        _("Employee Branch"), max_length=150, null=True, blank=True
    )
    employee_level = models.CharField(
        _("Employee Level"), max_length=50, null=True, blank=True
    )
    date_applied = models.DateField(_("Date Applied"), default=timezone.now)
    status = models.CharField(_("Status"), max_length=150, null=True, blank=True)
    hod_status = models.PositiveIntegerField(_("HOD Status"), null=True, blank=True)
    hod_remarks = models.CharField(
        _("HOD Remarks"), max_length=250, null=True, blank=True
    )
    relieving_officer_name = models.CharField(
        _("Relieving Officer Name"), max_length=250, null=True, blank=True
    )
    hod_remarks_date = models.CharField(_("HOD Remarks Date"), blank=True, null=True)
    hr_status = models.PositiveIntegerField(_("HR Status"), blank=True, null=True)
    hr_remarks = models.CharField(_("HR Remarks"), max_length=50, null=True, blank=True)
    hr_remarks_date = models.CharField(_("HR Remarks Date"), blank=True, null=True)
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    dep_code = models.CharField(
        _("Department Code"), max_length=50, null=True, blank=True
    )
    dep = models.CharField(_("Department"), max_length=50, null=True, blank=True)
    supporting_doc = models.TextField(_("Supporting Document"), null=True, blank=True)
    no_of_days_left = models.PositiveIntegerField(
        _("Number of Days Left"), null=True, blank=True
    )
    emp_code = models.CharField(
        _("Employee Code"), max_length=50, null=True, blank=True
    )
    leave_reason = models.CharField(_("Leave Reason"), max_length=250, blank=True, null=True)

    class Meta:
        abstract = True


class LeaveRequest(LeaveBase):
    is_extend = models.PositiveIntegerField(_("Requestion for Extension"), blank=True, null=True,default=0)
    no_of_extension_days = models.PositiveIntegerField(_("No Of Extension Days"), blank=True, null=True)
    hr_extension_status = models.PositiveIntegerField(_("HR Extension Status"), blank=True, null=True, default=0)
    hod_extension_status = models.PositiveIntegerField(_("HOD Extension Status"), blank=True, null=True, default=0)
    date_of_extension = models.CharField(_("Date of Extension"), null=True, blank=True, max_length=250)
    hod_extension_date = models.CharField(_("HOD Extension Date"), null=True, blank=True, max_length=250)
    hr_extension_date = models.CharField(_("HR Extension Date"), null=True, blank=True, max_length=250)
    hod_extension_remarks = models.CharField(_("HOD Extension Remarks"), max_length=250, blank=True, null=True)
    hr_extension_remarks = models.CharField(_("HR Extension Remarks"), max_length=250, blank=True, null=True)
    total_number_of_leave_days = models.PositiveIntegerField(_("Total Number Of Leave Days"), null=True, blank=True)
    hod_extension_status = models.PositiveIntegerField(_("HOO Extension Status"), null=True, blank=True)
    extension_status = models.PositiveIntegerField(_("Extension Status"),default=0, null=True, blank=True)
    extension_reason = models.CharField(_("Extension Reason"), max_length=250, null=True, blank=True)

    @property
    def end_date(self):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        current_date = datetime.now().date()
        start_date = max(self.start_date, current_date)
        days_added = 0

        while days_added < self.no_of_days_requested:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5 or start_date in holidays:
                continue
            days_added += 1
        return start_date
    
    @property
    def extension_date(self):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        start_date = self.end_date
        current_date = datetime.now().date()
        new_start_date = max(current_date, start_date)
        days_added = 0

        if self.no_of_extension_days is not None:
            while days_added < self.no_of_extension_days:
                new_start_date += timedelta(days=1)
                if new_start_date.weekday() >= 5 or new_start_date in holidays:
                    continue
                days_added += 1

        return new_start_date


    def clean(self):
        employee = self.employee  # get the currently selected employee
        max_days = self.leave_type.calculate_max_days(employee)

        if self.leave_type.name == "Maternity":
            self.no_of_days_requested = self.leave_type.max_number_of_days
            self.no_of_days_left = self.employee.days_left

        if self.leave_type.name == "Medical":
            self.no_of_days_requested = self.no_of_days_requested
            emp_days_left = employee.days_left
            if emp_days_left is not None:
                if self.no_of_days_requested <= emp_days_left:
                    self.no_of_days_left = emp_days_left - self.no_of_days_requested
                elif self.no_of_days_requested > emp_days_left:
                    raise ValidationError(
                        f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
                    )

        elif self.leave_type.name == "Annual":
            emp_days_left = employee.days_left
            if emp_days_left is not None:
                if self.no_of_days_requested <= emp_days_left:
                    self.no_of_days_left = emp_days_left - self.no_of_days_requested
                elif self.no_of_days_requested > emp_days_left:
                    raise ValidationError(
                        f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
                    )

        no_of_days_exhausted = self.employee.no_of_days_exhausted or 0
        no_of_days_exhausted += self.no_of_days_requested


        self.emp_code = employee.code
        self.employee_branch = employee.third_category_level
        self.job_title = employee.job_title
        self.dep = employee.first_category_level
        self.employee_unit = employee.second_category_level

        if self.is_extend == 1:
            if self.leave_type.name == "Medical":
                employee = self.employee
                emp_days_left = employee.days_left
                if emp_days_left is not None:
                    if self.no_of_extension_days <= emp_days_left:
                        self.no_of_days_left = emp_days_left - self.no_of_days_requested
                    elif self.no_of_extension_days > emp_days_left:
                        raise ValidationError(
                            f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
                        )

            elif self.leave_type.name == "Annual":
                emp_days_left = employee.days_left
                if emp_days_left is not None:
                    if self.no_of_extension_days <= emp_days_left:
                        self.no_of_days_left = emp_days_left - self.no_of_days_requested
                    elif self.no_of_extension_days > emp_days_left:
                        raise ValidationError(
                            f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
                        )

        if employee.no_of_days_exhausted == max_days:
            raise ValueError(
                f"Number of Days Exhausted {employee.no_of_days_exhausted} == Maxdays {max_days} "
            )
        else:
            self._meta.get_field("no_of_days_requested").editable = True
        


    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"

    def __str__(self):
        return f"{self.leave_type}, {self.start_date} - {self.no_of_days_requested}"


class LeavePlan(LeaveBase):

    @property
    def end_date(self):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        current_date = datetime.now().date()
        start_date = max(self.start_date, current_date)
        days_added = 0

        while days_added < self.no_of_days_requested:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5 or start_date in holidays:
                continue
            days_added += 1
        return start_date

    def clean(self):
        employee = self.employee  # get the currently selected employee
        max_days = self.leave_type.calculate_max_days(employee)

        if self.leave_type.name == "Maternity":
            self.no_of_days_requested = self.leave_type.max_number_of_days
            self.no_of_days_left = self.employee.plan_days_left

        elif self.leave_type.name == "Medical":
            self.no_of_days_requested = self.no_of_days_requested
            employee = self.employee
            emp_days_left = employee.plan_days_left
            if emp_days_left is not None:
                if self.no_of_days_requested <= emp_days_left:
                    self.no_of_days_left = emp_days_left - self.no_of_days_requested
                elif self.no_of_days_requested > emp_days_left:
                    raise ValidationError(
                        f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
                    )

        elif self.leave_type.name == "Annual":
            self.no_of_days_requested = self.no_of_days_requested

            employee = self.employee
            emp_days_left = employee.plan_days_left
            if emp_days_left is not None:
                if self.no_of_days_requested <= emp_days_left:
                    self.no_of_days_left = emp_days_left - self.no_of_days_requested

                elif self.no_of_days_requested > emp_days_left:
                    raise ValidationError(
                        f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
                    )

        no_of_days_exhausted = self.employee.plan_no_of_days_exhausted or 0
        no_of_days_exhausted += self.no_of_days_requested

        self.emp_code = employee.code
        self.employee_branch = employee.third_category_level
        self.job_title = employee.job_title
        self.dep = employee.first_category_level
        self.employee_unit = employee.second_category_level

        if employee.no_of_days_exhausted == max_days:
            raise ValueError(
                f"Number of Days Exhausted {employee.no_of_days_exhausted} == Maxdays {max_days} "
            )
        else:
            self._meta.get_field("no_of_days_requested").editable = True

    def save(self, *args, **kwargs):
        if self.hr_status == 2:
            if self.leave_type.name == "Maternity":
                self.no_of_days_requested = self.leave_type.max_number_of_days
                self.no_of_days_left = self.employee.plan_days_left

            if self.leave_type.name == "Medical":
                self.no_of_days_requested = self.no_of_days_requested
                employee = self.employee
                emp_days_left = employee.plan_days_left
                if emp_days_left is not None:
                    if self.no_of_days_requested <= emp_days_left:
                        self.no_of_days_left = emp_days_left - self.no_of_days_requested



            elif self.leave_type.name == "Annual":
                self.no_of_days_requested = self.no_of_days_requested

                employee = self.employee
                emp_days_left = employee.plan_days_left
                if emp_days_left is not None:
                    if self.no_of_days_requested <= emp_days_left:
                        self.no_of_days_left = emp_days_left - self.no_of_days_requested

            no_of_days_exhausted = self.employee.plan_no_of_days_exhausted or 0
            no_of_days_exhausted += self.no_of_days_requested

            # update employee with new values of days_left and no_of_days_exhausted
            Employee.objects.filter(id=self.employee.id).update(
                days_left=self.no_of_days_left, no_of_days_exhausted=no_of_days_exhausted
            )
        super(LeavePlan, self).save(*args, **kwargs)


class LeaveType(models.Model):
    code = models.UUIDField(
        _("Code"), primary_key=True, editable=False, default=uuid.uuid4
    )
    name = models.CharField(_("Name"), max_length=50, blank=True, null=True)
    max_number_of_days = models.PositiveIntegerField(
        _("Max Number Of Days"), blank=True, null=True
    )
    staff_category = models.ForeignKey(
        "employee.StaffCategory", on_delete=models.CASCADE, null=True, blank=True
    )

    def calculate_max_days(self, employee):
        if self.name == "Medical":
            max_days = employee.days_left
        elif self.name == "Annual":
            max_days = employee.days_left
        else:
            max_days = self.max_number_of_days

        if self.staff_category == employee.staff_category_code:
            return max_days
        else:
            return 0

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"


if connection.vendor == "postgresql":
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT EXISTS(
                SELECT * FROM information_schema.columns
                WHERE table_name = 'leave_leavetype' AND column_name = 'staff_category'
            )
        """
        )
        column_exists = cursor.fetchone()[0]
        if column_exists:
            cursor.execute(
                "ALTER TABLE leave_leavetype ALTER COLUMN staff_category TYPE VARCHAR(50)"
            )


