# Generated by Django 4.1.7 on 2023-02-21 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paygroup', '0001_initial'),
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_code', models.CharField(max_length=50, verbose_name='Training Code')),
                ('emp_code', models.CharField(max_length=50, verbose_name='Employee Code')),
                ('expense_description', models.CharField(max_length=50, verbose_name='Expense Description')),
                ('currency_code', models.CharField(max_length=50, verbose_name='Currency Code')),
                ('budgeted_cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Budgeted Cost')),
                ('actual_cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Actual Cost')),
                ('expense_type', models.CharField(choices=[('PER INDIVIDUAL', 'Per Individual'), ('TOTAL COST', 'Total Cost')], max_length=50, verbose_name='Expense Type')),
            ],
            options={
                'verbose_name': 'Budget',
                'verbose_name_plural': 'Budgets',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Course Code')),
                ('description', models.TextField(verbose_name='Course Description')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_no', models.PositiveIntegerField(verbose_name='Entry No.')),
                ('no', models.PositiveIntegerField(verbose_name='No.')),
                ('course_description', models.CharField(max_length=100, verbose_name='Course Detail')),
                ('course_content', models.CharField(max_length=100, verbose_name='Course Content')),
            ],
            options={
                'verbose_name': 'Course Detail',
                'verbose_name_plural': 'Course Details',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Expense Code')),
                ('expense_name', models.CharField(max_length=50, verbose_name='Expense Name')),
                ('currency_code', models.CharField(max_length=50, verbose_name='CUrrency Code')),
                ('maximum_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Maximum Value')),
                ('blocked', models.BooleanField(verbose_name='Blocked')),
                ('expense_usage_type', models.CharField(choices=[('LOCAL', 'Local'), ('FOREIGN', 'Foreign')], max_length=50, verbose_name='Expense Usage Type')),
                ('expense_type', models.CharField(choices=[('PER INDIVIDUAL', 'Per Individual'), ('TOTAL COST', 'Total Cost')], max_length=50, verbose_name='Expnse TYpe')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Training Code')),
                ('emp_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Employee Code')),
                ('entry_no', models.PositiveIntegerField(blank=True, null=True, verbose_name='Entry No.')),
                ('training_outcome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Training Outcome')),
                ('remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('training_rating', models.CharField(choices=[('EXCELLENT', 'Excellent'), ('GOOD', 'Good'), ('AVERAGE', 'Average'), ('BELOW AVERAGE', 'Below Average'), ('POOR', 'Poor')], max_length=50, verbose_name='Training Rating')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Organizers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Organizer Code')),
                ('name', models.CharField(max_length=200, verbose_name='Name Of Organizer')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('address2', models.CharField(max_length=50, verbose_name='Address 2')),
                ('contact_number', models.CharField(max_length=50, verbose_name='Contact Number')),
            ],
            options={
                'verbose_name': 'Organizers',
                'verbose_name_plural': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_code', models.CharField(max_length=50, verbose_name='Training Code')),
                ('emp_code', models.CharField(max_length=50, verbose_name='Employee Code')),
                ('course_code', models.CharField(max_length=50, verbose_name='Course Code')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
            ],
            options={
                'verbose_name': 'Feddback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=50, verbose_name='Department Code')),
                ('course_code', models.CharField(max_length=50, verbose_name='Course Code')),
                ('training_facilitator', models.CharField(max_length=200, verbose_name='Training Facilitator')),
                ('organizer_code', models.CharField(max_length=50, verbose_name='Organizer Code')),
                ('training_type', models.CharField(choices=[('IN HOUSE', 'In House'), ('EXTERNAL', 'External'), ('OVERSEAS', 'Overseas')], max_length=50, verbose_name='Training Type')),
                ('training_venue', models.CharField(max_length=50, verbose_name='Training Venue')),
                ('training_schedule', models.CharField(choices=[('WEEKDAYS', 'Weekdays'), ('WEEKDAYS + SATURDAYS', 'Weekdays + Saturdays'), ('WEEKDAYS + WEEKENDS', 'WEEKDAYS + WEEKENDS')], max_length=50, verbose_name='Training Schedule')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('daily_start_time', models.TimeField(verbose_name='Daily Start Time')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
                ('no_series', models.CharField(max_length=50, verbose_name='No. Series')),
                ('currency_code', models.CharField(max_length=50, verbose_name='CUrrency')),
                ('total_budget_amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Budget Amount')),
                ('total_actual_amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Actual Amount')),
                ('variance_amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Variance Amount')),
                ('training_status', models.CharField(choices=[('PLAN', 'Plan'), ('SCHEDULED', 'Scheduled'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], max_length=50, verbose_name='Training Status')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_code', models.CharField(max_length=50, verbose_name='Training Code')),
                ('entry_no', models.PositiveIntegerField(verbose_name='Entry No.')),
                ('emp_code', models.CharField(max_length=50, verbose_name='Employee Code')),
                ('course_code', models.CharField(max_length=50, verbose_name='Course Code')),
                ('facilitator', models.CharField(max_length=200, verbose_name='Faciliator')),
                ('organizer_code', models.CharField(max_length=50, verbose_name='Organizer Code')),
                ('training_type', models.CharField(choices=[('INTERNAL', 'Internal'), ('EXTERNAL', 'External'), ('INTERNATIONAL', 'International')], max_length=50, verbose_name='Training Type')),
                ('training_venue', models.CharField(max_length=100, verbose_name='Training Venue')),
                ('training_schedule', models.CharField(choices=[('WEEKDAYS', 'Weekdays'), ('WEEKDAYS + SATURDAYS', 'Weekdays + Saturdays'), ('WEEKDAYS + WEEKENDS', 'WEEKDAYS + WEEKENDS')], max_length=50, verbose_name='Training Schedule')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('daily_start_time', models.TimeField(verbose_name='Daily Start Time')),
                ('dimension_code', models.CharField(max_length=50, verbose_name='Dimension Code')),
                ('dimension_value', models.CharField(max_length=50, verbose_name='Dimension Value')),
                ('approved', models.BooleanField(verbose_name='Approved')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainingapplication.course', verbose_name='Course Name')),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee Name')),
                ('organizer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainingapplication.organizers', verbose_name='')),
                ('paygroup_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paygroup.paygroup', verbose_name='PayGroup Code')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
    ]
