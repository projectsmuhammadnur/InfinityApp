# Generated by Django 5.0.1 on 2024-05-11 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0002_remove_parents_father_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parents',
            name='password',
        ),
    ]
