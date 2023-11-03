from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from apps.parser.models import Currency


class Command(BaseCommand):
    help = "Update currency rate by name"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)
        parser.add_argument("rate", type=float)

    def handle(self, *args, **options):
        name = options["name"]
        rate = options["rate"]
        try:
            currency = Currency.objects.get(name=name)
            currency.rate = rate
            currency.save()
            self.stdout.write(self.style.SUCCESS("Currency was successfully updated."))
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR("Currency with provided name does not exist."))
