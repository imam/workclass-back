from django.core.management.base import BaseCommand
from database.models import Job

class Command(BaseCommand):
    help = 'Repolpulate Jobs'

    def handle(self, *args, **kwargs):
        for job in Job.objects.all():
            job.save()