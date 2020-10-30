from django.shortcuts import render, redirect

from .models import Task, Space, SubTask, List
from django.urls import reverse_lazy
from django.contrib.auth.models import User


def main(request):
	space = Space.objects.all()
	return render(request, 'main/index.html', context = {'space':space})


