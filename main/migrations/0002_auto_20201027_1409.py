# Generated by Django 3.1.2 on 2020-10-27 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='assign',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assign',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.DeleteModel(
            name='InsideTask',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
