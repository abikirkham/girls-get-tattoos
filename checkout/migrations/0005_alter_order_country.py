# Generated by Django 5.1.1 on 2024-10-22 12:04

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_remove_order_original_bag_remove_order_stripe_pid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
