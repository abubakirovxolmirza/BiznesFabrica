# Generated by Django 5.0.6 on 2024-06-29 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_emailverification_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckGr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reyting',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('admin', models.CharField(blank=True, choices=[('General', 'General'), ('Mayor', 'Mayor'), ('Captain', 'Captain'), ('Leytenant', 'Leytenant'), ('Serjant', 'Serjant'), ('Kursant', 'Kursant'), ('Saldat', 'Saldat')], max_length=200, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('shiori', models.CharField(blank=True, max_length=200, null=True)),
                ('generate_code', models.CharField(blank=True, max_length=10, null=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gr_code', models.CharField(max_length=10, unique=True)),
                ('gr_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.group')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.group'),
        ),
    ]
