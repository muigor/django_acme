# Generated by Django 3.0 on 2023-02-23 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ue',
            name='prime',
        ),
    ]
