# Generated by Django 5.0.3 on 2024-03-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='field1',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
