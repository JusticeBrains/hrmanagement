from typing import Iterable, Optional
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime, timedelta
from django.utils import timezone


User = get_user_model()


class HolidayCalender(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=80)
    holiday_date = models.DateField(
        _("Holiday Date"), auto_now=False, auto_now_add=False
    )
    company = models.CharField(_("Company"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Holiday Calender"
        verbose_name_plural = "Holiday Calenders"

    def __str__(self):
        return f"{self.name} - {self.holiday_date}"


class LeaveBase(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
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
    hod_status = models.PositiveIntegerField(_("HOD Status"), default=0)
    hod_remarks = models.CharField(
        _("HOD Remarks"), max_length=250, null=True, blank=True
    )
    relieving_officer_name = models.CharField(
        _("Relieving Officer Name"), max_length=250, null=True, blank=True
    )
    hod_remarks_date = models.CharField(
        _("HOD Remarks Date"), blank=True, null=True, max_length=50
    )
    hr_status = models.PositiveIntegerField(_("HR Status"), default=0)
    hr_remarks = models.CharField(_("HR Remarks"), max_length=50, null=True, blank=True)
    hr_remarks_date = models.CharField(
        _("HR Remarks Date"), blank=True, null=True, max_length=50
    )
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    dep_id = models.CharField(
        _("Department ID"), max_length=50, null=True, blank=True
    )
    dep = models.CharField(_("Department"), max_length=50, null=True, blank=True)
    supporting_doc = models.TextField(_("Supporting Document"), null=True, blank=True)
    emp_code = models.CharField(
        _("Employee Code"), max_length=50, null=True, blank=True
    )
    leave_reason = models.CharField(
        _("Leave Reason"), max_length=250, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    resumption_date = models.DateField(_("Resumption Date"), null=True, blank=True)
    unique_code = models.CharField(
        _("Unique Code"), max_length=50, null=True, blank=True
    )
    period = models.CharField(_("Period"), max_length=50, default=timezone.now().year)
    is_maternity = models.PositiveIntegerField(_("Is Maternity"), default=0)
    unpaid_leave = models.PositiveIntegerField(_("Unpaid Leave"), default=0)
    accrued_leave = models.PositiveIntegerField(_("Accrued Leave"), default=0)
    class Meta:
        abstract = True


class LeaveRequest(LeaveBase):
    is_extend = models.PositiveIntegerField(
        _("Request for Extension"), blank=True, null=True, default=0
    )
    no_of_extension_days = models.PositiveIntegerField(
        _("No Of Extension Days"), blank=True, null=True
    )
    hr_extension_status = models.PositiveIntegerField(
        _("HR Extension Status"), blank=True, null=True, default=0
    )
    hod_extension_status = models.PositiveIntegerField(
        _("HOD Extension Status"), blank=True, null=True, default=0
    )
    date_of_extension = models.CharField(
        _("Date of Extension"), null=True, blank=True, max_length=250
    )
    hod_extension_date = models.CharField(
        _("HOD Extension Date"), null=True, blank=True, max_length=250
    )
    hr_extension_date = models.CharField(
        _("HR Extension Date"), null=True, blank=True, max_length=250
    )
    hod_extension_remarks = models.CharField(
        _("HOD Extension Remarks"), max_length=250, blank=True, null=True
    )
    hr_extension_remarks = models.CharField(
        _("HR Extension Remarks"), max_length=250, blank=True, null=True
    )
    hod_extension_status = models.PositiveIntegerField(
        _("HOD Extension Status"), null=True, blank=True
    )
    extension_status = models.PositiveIntegerField(
        _("Extension Status"), default=0, null=True, blank=True
    )
    extension_reason = models.CharField(
        _("Extension Reason"), max_length=250, null=True, blank=True
    )
    unpaid_leave_days = models.PositiveIntegerField(
        _("Unpaid Leave Days"), blank=True, null=True, default=0
    )

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

    @property
    def resumption_date(self):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        calculated_resumption_date = self.end_date + timedelta(days=1)
        resumption_date = calculated_resumption_date
        while resumption_date in holidays or resumption_date.weekday() >= 5:
            resumption_date += timedelta(days=1)
        return resumption_date

    @resumption_date.setter
    def resumption_date(self, value):
        self._resumption_date = value


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

    @property
    def resumption_date(self):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        calculated_resumption_date = self.end_date + timedelta(days=1)
        resumption_date = calculated_resumption_date
        while resumption_date in holidays or resumption_date.weekday() >= 5:
            resumption_date += timedelta(days=1)
        return resumption_date

    @resumption_date.setter
    def resumption_date(self, value):
        self._resumption_date = value


class LeaveType(models.Model):
    code = models.UUIDField(
        _("Code"), primary_key=True, editable=False, default=uuid.uuid4
    )
    name = models.CharField(_("Name"), max_length=50, blank=True, null=True)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    unique_code = models.CharField(
        _("Unique Code"), max_length=50, null=True, blank=True
    )
    unpaid_leave = models.PositiveIntegerField(_("Unpaid Leave"), blank=True, null=True)
    rollover = models.PositiveIntegerField(_("Rollover"), default=0)


    def __str__(self):
        return f"{self.name} - {self.company}"

    class Meta:
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"


# if connection.vendor == "postgresql":
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """
#             SELECT EXISTS(
#                 SELECT * FROM information_schema.columns
#                 WHERE table_name = 'leave_leavetype' AND column_name = 'staff_category'
#             )
#         """
#         )
#         column_exists = cursor.fetchone()[0]
#         if column_exists:
#             cursor.execute(
#                 "ALTER TABLE leave_leavetype ALTER COLUMN staff_category TYPE VARCHAR(50)"
#             )


class LeaveLimits(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    leave_type = models.ForeignKey(
        "leave.LeaveType",
        verbose_name=_("Leave Type"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    leave_name = models.CharField(_("Leave Name"), max_length=150, null=True, blank=True)
    paygroup = models.ForeignKey(
        "employee.PayGroup",
        verbose_name=_("Paygroup"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    paygroup_name = models.CharField(_("PayGroup Name"), max_length=150, blank=True, null=True)
    company_id = models.CharField(_("Company ID"), max_length=150, blank=True)
    max_number_of_days = models.PositiveIntegerField(
        _("Max Number of Days"), blank=True, null=True
    )
    period = models.CharField(_("Period"), max_length=80, blank=True, null=True, default=timezone.now().year)

    class Meta:
        unique_together = ("leave_type", "paygroup")
        verbose_name = "Leave Limits"
        verbose_name_plural = "Leave Limits"

    def __str__(self):
        return f"{self.leave_type}, {self.paygroup}"



class EmployeeLeaveLimits(models.Model):
    id = models.UUIDField(_("ID"), editable=False, primary_key=True, default=uuid.uuid4)
    leave_type = models.CharField(
        _("Leave Type"), max_length=150, blank=True, null=True
    )
    leave_type_id = models.CharField(_("Leave Type ID"), max_length=150, blank=True, null=True)
    employee = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    max_number_of_days = models.PositiveIntegerField(
        _("Max Number of Days"), blank=True, null=True, default=0
    )
    number_of_days_left = models.PositiveIntegerField(
        _("Number of Days Left"), blank=True, null=True, default=0
    )
    number_of_days_exhausted = models.PositiveIntegerField(_("Number of Days Exhausted"), default=0)
    number_of_plan_days_left = models.PositiveIntegerField(
        _("Number of Plan Days Left"), blank=True, null=True, default=0
    )
    number_of_plan_days_exhausted = models.PositiveIntegerField(_("Number of Plan Days Exhausted"), default=0)

    unpaid_leave_days = models.PositiveIntegerField(_("Unpaid Leave Days"), default=0)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    paygroup = models.ForeignKey(
        "employee.PayGroup",
        verbose_name=_("Paygroup"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    period = models.CharField(_("Period"), max_length=80, blank=True, null=True, default=timezone.now().year)
    rollover_days = models.PositiveIntegerField(_("Rollover Days"), null=True, blank=True)
    class Meta:
        # unique_together = (
        #     "leave_type",
        #     "employee",
        # )
        verbose_name = "Employee Leave Limits"
        verbose_name_plural = "Employee Leave Limits"

    def __str__(self):
        return f"{self.leave_type} - {self.employee} - {self.company}"
