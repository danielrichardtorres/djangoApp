# Generated by Django 4.0.5 on 2022-07-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
    ]