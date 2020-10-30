# Generated by Django 3.1.2 on 2020-10-27 14:09

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20201027_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Лист',
                'verbose_name_plural': 'Листы',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('dead_line', models.DateField()),
                ('attachments', models.FileField(blank=True, upload_to='files/')),
                ('status', models.CharField(choices=[('1', 'Начало'), ('2', 'В процессе'), ('3', 'Завершено')], default=1, max_length=7)),
                ('description', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('change_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('created_by', models.CharField(max_length=150)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.list')),
            ],
            options={
                'verbose_name': 'Таск',
                'verbose_name_plural': 'Таски',
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('dead_line', models.DateField()),
                ('attachments', models.FileField(blank=True, upload_to='files/')),
                ('status', models.CharField(choices=[('1', 'Начало'), ('2', 'В процессе'), ('3', 'Завершено')], default=1, max_length=7)),
                ('description', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('change_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('created_by', models.CharField(max_length=150)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
            ],
            options={
                'verbose_name': 'Под Таск',
                'verbose_name_plural': 'Под Таски',
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('1', 'Начало'), ('2', 'В процессе'), ('3', 'Завершено')], default=1, max_length=7)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now=True)),
                ('created_by', models.CharField(max_length=150)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.space'),
        ),
    ]