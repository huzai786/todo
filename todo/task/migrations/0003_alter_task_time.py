# Generated by Django 4.0.1 on 2022-01-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]
