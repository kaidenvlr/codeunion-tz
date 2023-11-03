import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from apps.parser.models import Currency
from apps.parser.serializers import CurrencySerializer


class Command(BaseCommand):
    help = "Update currency rate by name"

    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", type=str)

    def handle(self, *args, **options):
        name = options.get("name", None)
        if name:
            try:
                queryset = Currency.objects.get(name=name)
                serializer = CurrencySerializer(queryset)
                self.stdout.write(self.style.SUCCESS("Returned 1 row:"))
                self.stdout.write(json.dumps(serializer.data, indent=1))
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR("Currency with provided name does not exist."))
        else:
            queryset = Currency.objects.all()
            serializer = CurrencySerializer(queryset, many=True)
            count = queryset.count()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Returned {queryset.count()} rows:" if count != 1 else "Returned 1 row:"
                )
            )
            self.stdout.write(json.dumps(serializer.data, indent=2))
