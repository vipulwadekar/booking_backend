# Generated by Django 3.2.15 on 2022-09-12 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0016_booking_isbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='slot',
        ),
    ]