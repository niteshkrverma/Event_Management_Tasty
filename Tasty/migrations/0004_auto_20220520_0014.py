# Generated by Django 3.0.5 on 2022-05-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasty', '0003_booking_d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='D',
        ),
        migrations.AlterField(
            model_name='booking',
            name='fdate',
            field=models.DateField(),
        ),
    ]
