from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
from  django.contrib import messages


# Create your views here.

def index(request):
    tareas = Tarea.objects.filter(titulo__contains = request.GET.get('search', ''))
    context = {'tareas': tareas}
    return render(request, 'tareas/index.html', context)

def view(request, id):
    tarea = Tarea.objects.get(id=id)
    context = {'tarea': tarea}
    return render(request, 'tareas/detail.html', context)

def edit(request, id):
    tarea = Tarea.objects.get(id=id)

    if request.method=='GET':
       form = TareaForm(instance=tarea)
       context= {'form': form, 'id': id}
       return render(request, 'tareas/edit.html', context)
    
    if request.method=='POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
           form.save()
        
        messages.success(request, 'Tarea actualizada.') 
        context= {'form': form, 'id': id}  
        return render(request, 'tareas/edit.html', context)

def create(request):
    if request.method=='GET':
       form = TareaForm()
       context= {'form': form}
       return render(request, 'tareas/create.html', context)
    
    if request.method=='POST':
        form = TareaForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('tareas')
    
def delete(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('tareas')
