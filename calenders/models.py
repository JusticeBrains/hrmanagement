import uuid
from django.db import models
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _
from options.text_options import BonusRunType, BonusRun

import calendar


class PeriodYear(models.Model):
    year = models.PositiveIntegerField(_("Year"), blank=True, null=True)
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = "Period Year"
        verbose_name_plural = "Period Years"
        unique_together = ("year", "company")

    def __str__(self):
        return str(self.year or "")

    def __repr__(self):
        return str(self.year or "")

    def generate_calendar(self):
        cal = calendar.Calendar()
        year_calendar = {}

        for month in range(1, 13):
            month_calendar = cal.monthdayscalendar(self.year, month)

            # Remove days outside of the current month (days with value 0)
            cleaned_month_calendar = [
                [day for day in week if day != 0] for week in month_calendar
            ]

            year_calendar[month] = cleaned_month_calendar

        return year_calendar

    def get_days_in_month(self, month):
        return calendar.monthrange(self.year, month)[1]

    def create_periods(self):
        month_calendars = self.generate_calendar()
        for month, month_calendar in month_calendars.items():
            period = Period(
                period_year=self, month=month, month_calendar=month_calendar
            )
            period.populate_dates()
            period.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)  # Save the PeriodYear instance
            self.create_periods()


class Period(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    period_year = models.ForeignKey(
        PeriodYear, on_delete=models.CASCADE, blank=True, null=True
    )
    period_year_value = models.PositiveIntegerField(
        _("Period Year Value"), default=1990
    )
    month = models.PositiveIntegerField(_("Month"), blank=True, null=True)
    month_calendar = models.JSONField(_("Month Calendar"), blank=True, null=True)
    total_working_days = models.PositiveIntegerField(
        _("Total Working Days"), blank=True, null=True
    )
    total_working_hours = models.PositiveIntegerField(
        _("Total Working Hours"), blank=True, null=True
    )
    total_hours_per_day = models.DecimalField(
        _("Total Hours Per Day"), max_digits=5, decimal_places=2, default=0.0
    )
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    no_of_days = models.PositiveIntegerField(_("No Of Days"), blank=True, null=True)
    period_name = models.CharField(
        _("Period Name"), max_length=50, blank=True, null=True
    )
    period_code = models.CharField(
        _("Period Code"), max_length=50, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    status = models.PositiveIntegerField(_("Status"), default=0)
    process = models.BooleanField(_("Process"), default=False)
    MONTH_NAMES = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    user_id = models.ForeignKey(
        "users.CustomUser",
        verbose_name=_("Employee"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = _("Period")
        verbose_name_plural = _("Periods")
        unique_together = ("period_year", "start_date", "end_date", "company")

    def get_month_name(self):
        return self.MONTH_NAMES.get(self.month, "")

    def __str__(self):
        return f"{self.period_year.year} - {self.get_month_name()}"

    def count_working_days(self, start_date, end_date):
        total_days = (
            end_date - start_date
        ).days + 1  # Include the end_date in the count
        working_days = 0

        for day in range(total_days):
            current_day = start_date + timedelta(days=day)
            if (
                current_day.weekday() < 5
            ):  # Monday to Friday are considered weekdays (0 to 4)
                working_days += 1

        return working_days

    def populate_dates(self):
        if self.month_calendar:
            first_day = self.month_calendar[0][0]
            last_week = self.month_calendar[-1]
            last_day = last_week[-1] if last_week[-1] != 0 else last_week[-2]
            days_in_month = self.period_year.get_days_in_month(self.month)
            self.no_of_days = days_in_month
            self.period_year_value = self.period_year.year
            self.user_id = self.period_year.user_id

            if 1 <= first_day <= 31 and 1 <= last_day <= 31:
                self.start_date = date(self.period_year.year, self.month, first_day)
                self.end_date = date(self.period_year.year, self.month, last_day)
                self.period_code = f"{self.MONTH_NAMES.get(self.month)[:3].upper()}{self.period_year.year}"
                self.period_name = (
                    f"{self.MONTH_NAMES.get(self.month)} {self.period_year.year}"
                )
                self.company = self.period_year.company
                if self.total_working_days is None and self.total_hours_per_day == 0.0:
                    self.total_working_days = self.count_working_days(
                        self.start_date, self.end_date
                    )
                    self.total_working_hours = self.total_working_days * 8
                elif (
                    self.total_working_days is not None
                    and self.total_hours_per_day == 0.0
                ):
                    self.total_working_hours = self.total_working_days * 8
                elif (
                    self.total_working_days is not None
                    and self.total_hours_per_day > 0.0
                ):
                    self.total_working_hours = (
                        self.total_working_days * self.total_hours_per_day
                    )

    def save(self, *args, **kwargs):
        self.populate_dates()
        super().save(*args, **kwargs)


class GlobalInputs(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    current_period = models.ForeignKey("calenders.Period", verbose_name=_("Current Period"), on_delete=models.DO_NOTHING)
    current_year = models.PositiveIntegerField(_("Current Year"), blank=True, null=True)
    country_code = models.CharField(_("Country Code"), max_length=150, blank=True, null=True)
    payroll_rounding = models.DecimalField(_("Payroll Rounding"), max_digits=5, decimal_places=4, default=0.0001)
    maximum_no_of_dependant_benefit = models.PositiveIntegerField(_("Maximum Number Of Dependant Benfit"), default=3)
    annual_working_hours = models.DecimalField(_("Annual Working Hours"), max_digits=6, decimal_places=2, default=0.0)
    bonus_run_type = models.CharField(_("Bonus Run Type"),choices=BonusRunType.choices, max_length=50,default=BonusRunType.MONTHLY)
    bonus_run = models.CharField(_("Bonus Run"), choices=BonusRun.choices,max_length=50, default=BonusRun.SEPERATE)
    minimum_net_pay = models.DecimalField(_("Minimum Net Pay"), max_digits=5, decimal_places=2, default=0.00)
    backpay_period = models.ForeignKey("calenders.Period", verbose_name=_("Back Pay Period"), on_delete=models.DO_NOTHING, related_name="backpay", blank=True, null=True)
    company = models.ForeignKey("company.Company",verbose_name="Company", on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Global Inputs"
        verbose_name_plural = "Global Inputs"

    def __str__(self):
        return f"{self.current_year}"

    def __repr__(self):
        return f"{self.current_year}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            GlobalInputs.objects.filter(company=self.company).delete()
        super().save(*args, **kwargs)