# Generated by Django 4.1.1 on 2022-09-23 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findtalent', '0002_individual_github_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='compatibility',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='surname',
        ),
    ]
