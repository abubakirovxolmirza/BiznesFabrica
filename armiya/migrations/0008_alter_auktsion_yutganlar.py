# Generated by Django 5.0.7 on 2024-07-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armiya', '0007_tranzaksiya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auktsion',
            name='yutganlar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]