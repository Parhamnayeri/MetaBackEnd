# Generated by Django 4.2.4 on 2024-18-03 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_id_alter_booking_num_of_guests_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='num_of_guests',
            new_name='no_of_guests',
        ),
    ]