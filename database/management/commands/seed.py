import json
from django.core.management.base import BaseCommand
from database.models import Job

'''
Database seeding
'''


class Command(BaseCommand):
    help = 'Seed the database'

    def handle(self, *args, **kwargs):
        with open('./data.json') as f:
            data = json.load(f)
        
        for job in data:
            j = Job(**job)
            j.save()
