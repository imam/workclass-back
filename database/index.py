import algoliasearch_django as algoliasearch

from .models import Job

algoliasearch.register(Job)