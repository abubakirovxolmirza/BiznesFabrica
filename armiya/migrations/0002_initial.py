# Generated by Django 5.0.7 on 2024-07-21 05:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('armiya', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='talablar',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='balls',
            name='tasks_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armiya.tasks'),
        ),
        migrations.AddField(
            model_name='taskusers',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armiya.tasks'),
        ),
        migrations.AddField(
            model_name='taskusers',
            name='users',
            field=models.ManyToManyField(related_name='armiya_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
