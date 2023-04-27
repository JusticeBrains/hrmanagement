from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime, timedelta

from options import text_options

User = get_user_model()


class Policy(models.Model):
    code = models.CharField(_("Code"), max_length=50, blank=True, null=True)
    description = models.CharField(_("Description"), max_length=100, blank=True, null=True)
    job_level_code = models.CharField(_("Job Level Code"), max_length=50)
    job_title = models.ForeignKey("company.Job", verbose_name=_("Job Title"), on_delete=models.CASCADE)
    no_of_days = models.PositiveIntegerField(_("No. Of Days"))
    accrued = models.BooleanField(_("Accrued"))
    automatically_roll_over = models.BooleanField(_("Automatically"))
    blocked = models.BooleanField(_("Blocked"))

    class Meta:
        verbose_name = "Policy"
        verbose_name_plural = 'Policies'

    def __str__(self):
        return f"{self.description}, {self.code}"


class Assignment(models.Model):
    input_option = models.CharField(_("Input Option"), max_length=50)
    input_code = models.CharField(_("Input Code"), max_length=50)
    leave_code = models.CharField(_("Leave Code"), max_length=50)
    leave_description = models.ForeignKey("Policy", verbose_name=_("Leave Description"), on_delete=models.CASCADE)
    no_of_days = models.PositiveIntegerField(_("No. Of Days"))
    accrued = models.BooleanField(_("Accrued"))
    automatically_roll_over = models.BooleanField(_("Automatically Roll Over"))
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    def __str__(self):
        return f"{self.input_code}, {self.leave_description}"


class RequestTransaction(models.Model):
    no = models.CharField(_("No."), max_length=50)
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE)
    emp_name = models.CharField(_("Employee Name"), max_length=50)
    contact_address = models.CharField(_("Contact Text"), max_length=50, blank=True, null=True)
    phone_number = models.CharField(_("Phone No."), max_length=50)
    leave_code = models.ForeignKey("Policy", verbose_name=_("Leave Code"), on_delete=models.CASCADE)
    leave_description = models.TextField(_("Leave Description"))
    total_leave_days = models.PositiveIntegerField(_("Total Leave Days"))
    outstanding_leave_days = models.PositiveIntegerField(_("Outstanding Leave Days"))
    no_of_days_requested = models.PositiveIntegerField(_("No. Of Days Requested"))
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    request_status = models.CharField(_("Request Status"), choices=text_options.LEAVEREQUESTSTATUS.choices,
                                      max_length=50)
    deferred_reason = models.TextField(_("Deferred Reason"))
    transaction_date = models.DateField(_("Transaction"), auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    relieving_officer_no = models.CharField(_("Relieving Officer No."), max_length=50)
    relieving_officer_name = models.CharField(_("Relieving Officer's Name"), max_length=150)
    posted = models.BooleanField(_("Posted"))
    job_title_code = models.ForeignKey("company.Job", verbose_name=_("Job Title Code"), on_delete=models.CASCADE)
    department_code = models.ForeignKey("company.Department", verbose_name=_("Department"), on_delete=models.CASCADE,
                                        blank=True, null=True)

    class Meta:
        abstract = True


class LeaveRequest(RequestTransaction):
    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"

    def __str__(self):
        return f"{self.emp_name}, {self.emp_code}, {self.start_date}"


class LeaveTransaction(RequestTransaction):
    reason_recall = models.BooleanField(_("Recalled"), blank=True, null=True)
    reason_for_recall = models.CharField(_("Reason For Recall"), max_length=100)
    approved_from_deferred = models.BooleanField(_("Approved From Deferred"))
    recall_amount = models.DecimalField(_("Recall Amount"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Leave Transaction"
        verbose_name_plural = "Leave Transactions"

    def __str__(self):
        return f"{self.reason_for_recall}, {self.reason_recall}"


class LeavePlan(models.Model):
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE)
    emp_name = models.CharField(_("Employee Name"), max_length=200)
    leave_code = models.CharField(_("Leave Code"), max_length=50)
    leave_description = models.CharField(_("Leave Description"), max_length=50)
    no_of_planned_days = models.PositiveIntegerField(_("No. Of Planned Days"))
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    department_code = models.ForeignKey("company.Department", verbose_name=_("Department Code"),
                                        on_delete=models.CASCADE)
    department_name = models.CharField(_("Department Name"), max_length=50)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    posted = models.BooleanField(_("Posted"))


    @property
    def end_date(self):
        current_date = datetime.now().date()
        start_date = max(self.start_date, current_date)
        days_added = 0

        while days_added < self.no_of_planned_days:
            start_date += timedelta(days=1)
            if start_date.weekday >= 5:
                continue
            days_added += 1
        return start_date

    class Meta:
        verbose_name = "Leave Plan"
        verbose_name_plural = "Leave Plans"

    def __str__(self):
        return f"{self.no_of_planned_days} - {self.end_date}"


class LeaveType(models.Model):
    code = models.UUIDField(_("Code"), primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"

    def __str__(self):
        return f"{self.code} - {self.name}"


class LeaveLimits(models.Model):
    code = models.UUIDField(_("Code"), primary_key=True, editable=False, default=uuid.uuid4)
    staff_category = models.CharField(_("Staff Category"), max_length=50)
    leave_type = models.ForeignKey("leave.LeaveType", verbose_name=_("Leave Type"), on_delete=models.CASCADE)
    no_of_days_allowed = models.PositiveIntegerField(_("No. Of Days Allowed"))

    class Meta:
        verbose_name = "Leave Limits"
        verbose_name_plural = "Leave Limits"

    def __str__(self):
        return f"{self.leave_type} - {self.no_of_days_allowed}"


class LeaveLedger(models.Model):
    employee = models.ForeignKey("employee.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE)
    leave_type = models.ForeignKey("leave.LeaveType", verbose_name=_("Leave Type"), on_delete=models.CASCADE)
    no_of_days_taken = models.PositiveIntegerField(_("No. Of Days Taken"))
    limit = models.PositiveIntegerField(_("Leave Limit"))

    class Meta:
        verbose_name = "Leave Ledger"
        verbose_name_plural = "Leave Ledgers"
    
    def __str__(self):
        return f"{self.employee} - {self.leave_type}"