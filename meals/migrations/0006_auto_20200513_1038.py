# Generated by Django 2.1.4 on 2020-05-13 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]