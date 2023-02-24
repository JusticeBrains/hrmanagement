from options import text_options

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    code = models.CharField(_("Course Code"), max_length=50)
    description = models.TextField(_("Course Description"))

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return f"{self.code}, {self.description}"


class CourseDetail(models.Model):
    course_code = models.ForeignKey("Course", verbose_name=_("Course Code"), on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    no = models.PositiveIntegerField(_("No."))
    course_description = models.CharField(_("Course Detail"), max_length=100)
    course_content = models.CharField(_("Course Content"), max_length=100)

    class Meta:
        verbose_name = "Course Detail"
        verbose_name_plural = "Course Details"

    def __str__(self):
        return f"{self.course_description}, {self.course_content}"


class Organizers(models.Model):
    code = models.CharField(_("Organizer Code"), max_length=50)
    name = models.CharField(_("Name Of Organizer"), max_length=200)
    address = models.CharField(_("Address"), max_length=50)
    address2 = models.CharField(_("Address 2"), max_length=50)
    contact_number = models.CharField(_("Contact Number"), max_length=50)

    class Meta:
        verbose_name = "Organizers"
        verbose_name_plural = "Organizers"

    def __str__(self):
        return self.name


class Plan(models.Model):
    department_code = models.CharField(_("Department Code"), max_length=50)
    department_name = models.ForeignKey("company.Department", verbose_name=_("Department Name"),
                                        on_delete=models.CASCADE)
    course_code = models.CharField(_("Course Code"), max_length=50)
    course_name = models.ForeignKey("Course", verbose_name=_("Course Name"), on_delete=models.CASCADE)
    training_facilitator = models.CharField(_("Training Facilitator"), max_length=200)
    organizer_code = models.CharField(_("Organizer Code"), max_length=50)
    organizer_name = models.ForeignKey("Organizers", verbose_name=_("Organizer Name"), on_delete=models.CASCADE)
    training_type = models.CharField(_("Training Type"), choices=text_options.TrainingType.choices, max_length=50)
    training_venue = models.CharField(_("Training Venue"), max_length=50)
    training_schedule = models.CharField(_("Training Schedule"), choices=text_options.TrainingSchedule.choices,
                                         max_length=50)
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    daily_start_time = models.TimeField(_("Daily Start Time"), auto_now=False, auto_now_add=False)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    no_series = models.CharField(_("No. Series"), max_length=50)
    currency_code = models.CharField(_("CUrrency"), max_length=50)
    total_budget_amount = models.DecimalField(_("Total Budget Amount"), max_digits=5, decimal_places=2)
    total_actual_amount = models.DecimalField(_("Total Actual Amount"), max_digits=5, decimal_places=2)
    variance_amount = models.DecimalField(_("Variance Amount"), max_digits=5, decimal_places=2)
    training_status = models.CharField(_("Training Status"), choices=text_options.TrainingStatus.choices, max_length=50)

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"

    @property
    def number_of_training_days(self):
        return self.end_date - self.start_date

    def __str__(self):
        return f"{self.organizer_name},{self.course_name}, {self.department_name}"


class Expense(models.Model):
    code = models.CharField(_("Expense Code"), max_length=50)
    expense_name = models.CharField(_("Expense Name"), max_length=50)
    currency_code = models.CharField(_("CUrrency Code"), max_length=50)
    maximum_value = models.DecimalField(_("Maximum Value"), max_digits=5, decimal_places=2)
    blocked = models.BooleanField(_("Blocked"))
    expense_usage_type = models.CharField(_("Expense Usage Type"), choices=text_options.ExpenseUsageType.choices,
                                          max_length=50)
    expense_type = models.CharField(_("Expnse TYpe"), choices=text_options.ExpenseType.choices, max_length=50)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"


class Budget(models.Model):
    training_code = models.CharField(_("Training Code"), max_length=50)
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey("employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    expense_code = models.ForeignKey("Expense", verbose_name=_("Expense Code"), on_delete=models.CASCADE)
    expense_description = models.CharField(_("Expense Description"), max_length=50)
    currency_code = models.CharField(_("Currency Code"), max_length=50)
    budgeted_cost = models.DecimalField(_("Budgeted Cost"), max_digits=5, decimal_places=2)
    actual_cost = models.DecimalField(_("Actual Cost"), max_digits=5, decimal_places=2)
    expense_type = models.CharField(_("Expense Type"), choices=text_options.ExpenseType.choices, max_length=50)

    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"

    @property
    def variance(self):
        return abs(self.budgeted_cost - self.actual_cost)

    def __str__(self):
        return f"{self.training_code}, {self.budgeted_cost}, {self.actual_cost}"


class Request(models.Model):
    training_code = models.CharField(_("Training Code"), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey("employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    course_code = models.CharField(_("Course Code"), max_length=50)
    course_name = models.ForeignKey(Course, verbose_name=_("Course Name"), on_delete=models.CASCADE)
    facilitator = models.CharField(_("Faciliator"), max_length=200)
    organizer_code = models.CharField(_("Organizer Code"), max_length=50)
    organizer_name = models.ForeignKey("Organizers", verbose_name=_(""), on_delete=models.CASCADE)
    training_type = models.CharField(_("Training Type"), choices=text_options.RequestTrainingType.choices,
                                     max_length=50)
    training_venue = models.CharField(_("Training Venue"), max_length=100)
    training_schedule = models.CharField(_("Training Schedule"), choices=text_options.TrainingSchedule.choices,
                                         max_length=50)
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    daily_start_time = models.TimeField(_("Daily Start Time"), auto_now=False, auto_now_add=False)
    dimension_code = models.CharField(_("Dimension Code"), max_length=50)
    dimension_value = models.CharField(_("Dimension Value"), max_length=50)
    paygroup_code = models.ForeignKey("paygroup.PayGroup", verbose_name=_("PayGroup Code"), on_delete=models.CASCADE)
    approved = models.BooleanField(_("Approved"))
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"

    @property
    def total_training_days(self):
        return self.end_date - self.start_date


class Feedback(models.Model):
    training_code = models.CharField(_("Training Code"), max_length=50, blank=True, null=True)
    emp_code = models.CharField(_("Employee Code"), max_length=50, blank=True, null=True)
    emp_name = models.ForeignKey("employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No."), blank=True, null=True)
    training_outcome = models.CharField(_("Training Outcome"), max_length=200, blank=True, null=True)
    remarks = models.CharField(_("Remarks"), max_length=250, blank=True, null=True)
    training_rating = models.CharField(_("Training Rating"), choices=text_options.TrainingRating.choices, max_length=50)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.remarks


class Participants(models.Model):
    training_code = models.CharField(_("Training Code"), max_length=50)
    emp_code = models.CharField(_("Employee Code"), max_length=50)
    emp_name = models.ForeignKey("employee.Employee", verbose_name=_("Employee Name"), on_delete=models.CASCADE)
    paygroup_code = models.ForeignKey("paygroup.PayGroup", verbose_name=_("PayGroup Code"), on_delete=models.CASCADE)
    course_code = models.CharField(_("Course Code"), max_length=50)
    course_name = models.ForeignKey("Course", verbose_name=_("Course Name"), on_delete=models.CASCADE)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Feddback"
        verbose_name_plural = "Feedbacks"
        
