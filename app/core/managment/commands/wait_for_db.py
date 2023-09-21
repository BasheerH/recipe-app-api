'''
Django commands to wait for the database to be available 
'''

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Django commands to wait for the database
    """
    def handle(self, *args, **options):
        pass
