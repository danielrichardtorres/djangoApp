# Generated by Django 4.0.6 on 2022-07-14 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_client_signupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='signupdate',
            field=models.DateField(default=datetime.date(2022, 7, 14), verbose_name='Sign Up Date'),
        ),
    ]
