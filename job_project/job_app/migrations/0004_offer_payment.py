# Generated by Django 4.2.1 on 2023-06-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0003_alter_offer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='payment',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
