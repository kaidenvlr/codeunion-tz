# Generated by Django 4.2.7 on 2023-11-03 20:37
# pylint: skip-file
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_alter_currency_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=3, unique=True, verbose_name='Currency name'),
        ),
    ]
