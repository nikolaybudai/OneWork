# Generated by Django 4.2.1 on 2023-06-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_offer_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='client',
        ),
        migrations.AddField(
            model_name='offer',
            name='phone_number',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
