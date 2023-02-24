# Generated by Django 4.1.7 on 2023-02-21 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0003_initial'),
        ('leave', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavetransaction',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='department_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='emp_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee Code'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='job_title_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.job', verbose_name='Job Title Code'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='leave_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.policy', verbose_name='Leave Code'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
        migrations.AddField(
            model_name='leaveplan',
            name='department_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='Department Code'),
        ),
        migrations.AddField(
            model_name='leaveplan',
            name='emp_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee Code'),
        ),
        migrations.AddField(
            model_name='leaveplan',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='leave_description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.policy', verbose_name='Leave Description'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
    ]
