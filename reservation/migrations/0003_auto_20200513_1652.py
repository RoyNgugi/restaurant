# Generated by Django 2.1.4 on 2020-05-13 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]