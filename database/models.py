from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save
from api.utils import check_job_type, check_employment_type

class Job(models.Model):
  class SalaryPeriodChoice(models.TextChoices):
      monthly = "monthly"
      hourly = "hourly"
      weekly = "weekly"
      yearly = "yearly"

  job_id = models.AutoField(primary_key=True, unique=True)

  # Job Details
  title = models.CharField(max_length=400)
  description = models.TextField()
  activation_date = models.DateTimeField(default=timezone.now)
  active = models.BooleanField()
  featured = models.BooleanField()
  salary_from = models.FloatField(null=True)
  salary_period = models.CharField(max_length=7, choices=SalaryPeriodChoice.choices)
  salary_to = models.FloatField(null=True)
  job_type = models.CharField(null=True, max_length=400)
  employment_type = models.CharField(null=True, max_length=400)

  # Company Details
  company_name = models.CharField(max_length=400)
  logo_url = models.CharField(max_length=500)

  # Job Categories
  job_admin = models.BooleanField(default=False)
  job_customerservice = models.BooleanField(default=False)
  job_distributionshipping = models.BooleanField(default=False)
  job_grocery = models.BooleanField(default=False)
  job_hospitalityhotel = models.BooleanField(default=False)
  job_covid19 = models.BooleanField(default=False)
  job_marketingsales = models.BooleanField(default=False)
  job_other = models.BooleanField(default=False)
  job_production = models.BooleanField(default=False)
  job_restaurantfoodservice = models.BooleanField(default=False)
  job_retail = models.BooleanField(default=False)
  job_supplychain = models.BooleanField(default=False)
  job_transportation = models.BooleanField(default=False)
  job_warehouse = models.BooleanField(default=False)

  # Employment Type
  employ_fulltime = models.BooleanField(default=False)
  employ_contract = models.BooleanField(default=False)
  employ_parttime = models.BooleanField(default=False)
  employ_adhoc = models.BooleanField(default=False)
  employ_internship = models.BooleanField(default=False)

  def values(self):
    return model_to_dict(self)

"""
Populate Job Type Field Before Saving
"""
@receiver(pre_save, sender=Job, dispatch_uid='update_job_field')
def update_job_field(sender, instance, **kwargs):
  instance.job_type = check_job_type(instance)

"""
Populate Employment Type Field Before Saving
"""
@receiver(pre_save, sender=Job, dispatch_uid='update_employment_field')
def update_job_field(sender, instance, **kwargs):
  instance.employment_type = check_employment_type(instance)