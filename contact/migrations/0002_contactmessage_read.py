# Generated by Django 4.2 on 2024-11-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
