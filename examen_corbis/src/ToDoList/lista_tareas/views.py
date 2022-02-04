from django.shortcuts import render, redirect, HttpResponse
from .models import Tareas
from .forms import FormTarea, CustomUserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Tareas
import datetime





# Create your views here.


def index(request):
    tareas = Tareas.objects.all()
    form = FormTarea()

    if request.method == 'POST':
        form = FormTarea(request.POST)
        if form.is_valid():
            form = form.save(commit=False)

            form.usuario_id = request.user.id
            
            form.save()
        return redirect('/')

    return render(request, 'index/index.html', {'form' : form, 'tareas' : tareas})


def editar_tarea(request, pk):
    tarea = Tareas.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == 'POST':
        form = FormTarea(request.POST, instance=tarea)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index/editar_tarea.html', {'form' : form})


def eliminar_tarea(request, pk):
    tarea = Tareas.objects.get(id=pk)

    if request.method == 'POST':
        tarea.delete()
        return redirect('/')

    return render(request, 'index/eliminar_tarea.html', {'tarea' : tarea})

