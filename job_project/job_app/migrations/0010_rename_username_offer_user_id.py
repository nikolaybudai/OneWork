# Generated by Django 4.2.1 on 2023-06-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0009_offer_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='username',
            new_name='user_id',
        ),
    ]