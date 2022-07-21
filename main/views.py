from django.http import Http404
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')[:1]
    context = {
        'title': 'Главная страница',
        'tasks': tasks
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
