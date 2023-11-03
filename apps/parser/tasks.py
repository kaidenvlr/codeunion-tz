import requests
import xmltodict
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.db import transaction

from .models import Currency

logger = get_task_logger(__name__)


@shared_task
def refresh_rate():
    with transaction.atomic():
        try:
            response = requests.get(settings.CURRENCY_URL)
            data = xmltodict.parse(response.text)
            if response.status_code == 200:
                data = data["rss"]["channel"]["item"]
                for currency in data:
                    name = currency.get("title")
                    rate = float(currency.get("description"))
                    currency, _ = Currency.objects.get_or_create(name=name)
                    currency.rate = rate
                    currency.save()
                return True
            else:
                print(data)
                return False
        except Exception as e:
            print(f"An error occured: {e}")
            return False
