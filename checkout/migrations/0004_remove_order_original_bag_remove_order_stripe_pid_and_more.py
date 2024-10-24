# Generated by Django 5.1.1 on 2024-10-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_original_bag_order_stripe_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
    ]