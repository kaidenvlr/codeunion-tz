"""
CLI Command
"""
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from apps.parser.models import Currency


class Command(BaseCommand):
    """Update currency command"""
    help = "Update currency rate by name"

    def add_arguments(self, parser):
        """
        Add CLI Command arguments
        """
        parser.add_argument("id", type=int)
        parser.add_argument("rate", type=float)

    def handle(self, *args, **options):
        """
        Handler to catch CLI Command
        """
        pk = options["id"]
        rate = options["rate"]
        try:
            currency = Currency.objects.get(pk=pk)
            currency.rate = rate
            currency.save()
            self.stdout.write("Currency was successfully updated.")
        except ObjectDoesNotExist:
            self.stdout.write("Currency with provided name does not exist.")
