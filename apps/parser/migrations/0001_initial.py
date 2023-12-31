# Generated by Django 4.2.7 on 2023-11-03 19:07
# pylint: skip-file
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='Currency name')),
                ('rate', models.FloatField(verbose_name='Currency rate')),
            ],
        ),
    ]
