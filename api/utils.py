from django.http import HttpResponse
from datetime import datetime, date, timedelta, time, timezone
import numpy as np
import json

job_types = {
    'job_admin': 'Admin',
    'job_customerservice': 'Customer Service',
    'job_distributionshipping': 'Distribution Shipping',
    'job_grocery': 'Grocery',
    'job_hospitalityhotel': 'Hospitality Hotel',
    'job_covid19': 'Covid 19',
    'job_marketingsales': 'Marketing Sales',
    'job_other': 'Other',
    'job_production': 'Production',
    'job_restaurantfoodservice': 'Restaurant Food Service',
    'job_retail': 'Retail',
    'job_supplychain': 'Supply Chain',
    'job_transportation': 'Transportation',
    'job_warehouse': 'Warehouse',
}

employment_types = {
    'employ_fulltime': 'Fulltime',
    'employ_contract': 'Contract',
    'employ_parttime': 'Part Time',
    'employ_adhoc': 'Ad Hoc',
    'employ_internship': 'Internship',
}

def jsonify(data):
	"""
	This function takes a valid dictionary and makes it into JSON format
	"""
	def dt_handler(obj):
		if isinstance(obj, (datetime, date, time)):
			return obj.isoformat()

		elif isinstance(obj, np.int64):
			return int(obj)

		elif isinstance(obj, timedelta):
			return obj.total_seconds()

		else:
			return None

	return HttpResponse(json.dumps(data, default=dt_handler))


def get_params(req):
	try:
			return req.GET.dict()
	except:
			return None

def get_data(req):
	try:
		return json.loads(req.body)
	except:
		return None

def check_job_type(job):
	job_type = None
	for type in job_types:
		if job.values()[type]:
			job_type = type	

	return job_types[job_type]

def check_employment_type(employment):
	employment_type = None
	for type in employment_types:
		if employment.values()[type]:
			employment_type = type	

	return employment_types[employment_type]

def convert_to_monthly(salary, recurring_type):
	if(recurring_type == "hourly"):
		return salary * 8 * 5 * 4
	if(recurring_type == "daily"):
		return salary * 5 * 4
	if(recurring_type == "weekly"):
		return salary * 5 * 4
	if(recurring_type == "yearly"):
		return salary / 12
	if(recurring_type == "monthly"):
		return salary
	return salary

def get_median_salary(job):
	salary_from_median = convert_to_monthly(job.salary_from, job.salary_period) if job.salary_from is not None else 0
	salary_to_median = convert_to_monthly(job.salary_to, job.salary_period) if job.salary_to is not None else 0

	return (salary_to_median + salary_from_median) / 2