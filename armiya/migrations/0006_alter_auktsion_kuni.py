# Generated by Django 5.0.7 on 2024-07-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armiya', '0005_alter_buyum_buyumusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auktsion',
            name='kuni',
            field=models.DateTimeField(),
        ),
    ]