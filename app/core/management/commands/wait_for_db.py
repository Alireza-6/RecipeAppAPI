import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OPError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OPError, OperationalError):
                self.stdout.write("Database unavailable wait one second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
