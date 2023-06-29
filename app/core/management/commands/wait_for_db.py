"""
Django commands for wait for database to be available.
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    '''Django Command to wait for database'''

    def handle(self, *args, **options):
        """Entry Point for command"""
        self.stdout.write("Waiting for Database......")
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, \
                                  waitng for 1 second....')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
