from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    task = Task.objects.all()
    return render(request,'task/main.html', {'title':'Главная страница','data' : task})

def about(request):
    return render(request,'task/about.html', {'title':'О нас','data':['Раз', 'Два', 'Три']})

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('home')
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('Error')

    form = TaskForm()
    context = {'form':form, 'title':'Добавить задачу'}
    return render(request,'task/create.html', context)

