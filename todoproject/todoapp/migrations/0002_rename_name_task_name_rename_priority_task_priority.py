# Generated by Django 5.0.3 on 2024-03-10 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='priority',
            new_name='Priority',
        ),
    ]