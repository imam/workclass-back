# Generated by Django 3.2.4 on 2021-07-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_job_employment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary_median',
            field=models.FloatField(null=True),
        ),
    ]
