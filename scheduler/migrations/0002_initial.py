# Generated by Django 4.0.5 on 2022-07-08 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_first_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_last_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(to='scheduler.subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.student'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.teacher'),
        ),
    ]