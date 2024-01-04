"""
CLI Command
"""
import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from apps.parser.models import Currency
from apps.parser.serializers import CurrencySerializer


class Command(BaseCommand):
    """
    Get currency CLI Command
    """
    help = "Update currency rate by name"

    def add_arguments(self, parser):
        """
        Add CLI command arguments
        """
        parser.add_argument("--id", type=int)

    def handle(self, *args, **options):
        """
        Handler to catch this CLI Command
        """
        pk = options.get("id", None)
        if pk:
            try:
                queryset = Currency.objects.get(pk=pk)
                serializer = CurrencySerializer(queryset)
                self.stdout.write("Returned 1 row:")
                self.stdout.write(json.dumps(serializer.data, indent=1))
            except ObjectDoesNotExist:
                self.stdout.write("Currency with provided name does not exist.")
        else:
            queryset = Currency.objects.all()
            serializer = CurrencySerializer(queryset, many=True)
            count = queryset.count()
            self.stdout.write(
                f"Returned {queryset.count()} rows:" if count != 1 else "Returned 1 row:"
            )
            self.stdout.write(json.dumps(serializer.data, indent=2))
