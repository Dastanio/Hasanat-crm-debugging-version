from django.db import models
from django.contrib.auth.models import User
import datetime
from colorfield.fields import ColorField

status = (
    ('1', 'Начало'),
    ('2', 'В процессе'),
    ('3', 'Завершено'),
)


class Space(models.Model):
    name = models.CharField('Название',max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)
    assign = models.ManyToManyField(User)
    status = models.CharField(max_length=7, choices=status, default=1)
    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)
    created_by = models.CharField(max_length=150)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return (self.name)

class List(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    name_list = models.CharField(max_length=100)
    created_by = models.CharField(max_length=150)
    def __str__(self):
        return (self.name_list)


class Task(models.Model):
    lists = models.ForeignKey(List, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=80)
    assign = models.ManyToManyField(User)
    dead_line = models.DateField()
    attachments = models.FileField(upload_to='files/',blank=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    change_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    created_by = models.CharField(max_length=150)

    def __str__(self):
        return(self.task_name)

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=80)
    assign = models.ManyToManyField(User)
    dead_line = models.DateField()
    attachments = models.FileField(upload_to='files/',blank=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    change_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    created_by = models.CharField(max_length=150)


    def __str__(self):
        return(self.task_name)

class TaskComment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment  = models.TextField(blank=True)

    def __str__(self):
        return(self.comment)

class SubTaskComment(models.Model):
    subtask = models.ForeignKey(SubTask,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment  = models.TextField(blank=True)

    def __str__(self):
        return(self.comment)

