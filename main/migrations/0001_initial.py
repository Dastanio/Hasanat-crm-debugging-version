# Generated by Django 3.1.2 on 2020-10-26 12:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, verbose_name='shortcut')),
                ('status', models.CharField(choices=[('1', 'Начало'), ('2', 'В процессе'), ('3', 'Завершено')], default=1, max_length=7)),
                ('dead_line', models.DateField()),
                ('complete_per', models.FloatField(max_length=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField(blank=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now=True)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('attachments', models.FileField(upload_to='files/')),
                ('status', models.CharField(choices=[('1', 'Начало'), ('2', 'В процессе'), ('3', 'Завершено')], default=1, max_length=7)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
            ],
            options={
                'ordering': ['project', 'task_name'],
            },
        ),
        migrations.CreateModel(
            name='InsideTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('attachments', models.FileField(upload_to='files/')),
                ('status', models.CharField(choices=[('1', 'Начало'), ('2', 'В процессе'), ('3', 'Завершено')], default=1, max_length=7)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
            ],
            options={
                'ordering': ['project', 'task_name'],
            },
        ),
    ]
