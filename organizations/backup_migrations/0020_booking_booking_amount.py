# Generated by Django 3.2.15 on 2022-09-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0019_rename_isbooking_booking_isbooked'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
