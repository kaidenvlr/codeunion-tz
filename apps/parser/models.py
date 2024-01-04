"""Models file of parser application"""
from django.db import models


class Currency(models.Model):
    """Currency model"""
    name = models.CharField(max_length=3, unique=True, verbose_name="Currency name")
    rate = models.FloatField(null=True, blank=True, verbose_name="Currency rate")

    def __str__(self):
        return f"{self.name} - {self.rate}"
