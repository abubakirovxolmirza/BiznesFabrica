# Generated by Django 5.0.6 on 2024-07-19 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armiya', '0009_rename_task_id_taskusers_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskusers',
            old_name='task',
            new_name='task_id',
        ),
    ]
