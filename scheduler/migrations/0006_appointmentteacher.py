# Generated by Django 4.0.6 on 2022-07-10 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_alter_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('order', models.IntegerField()),
                ('Appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.appointment')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.teacher')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
