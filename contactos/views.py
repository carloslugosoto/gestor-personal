from asyncio.windows_events import NULL
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def index(request, letter=None):  #NULL probar
    if letter != None:
        contactos = Contacto.objects.filter(nombre__istartswith = letter)
    else:    
        contactos = Contacto.objects.filter(nombre__contains = request.GET.get('search', ''))
    
    context = {'contactos': contactos}
    return render(request, 'contactos/index.html', context)

def view(request, id):
    contacto= Contacto.objects.get(id=id)
    context = {'contacto': contacto}
    return render(request, 'contactos/detail.html', context)

def edit(request, id):
    contacto= Contacto.objects.get(id=id)

    if request.method=='GET':
       form = ContactoForm(instance=contacto)
       context= {'form': form, 'id': id}
       return render(request, 'contactos/edit.html', context)
    
    if request.method=='POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
           form.save()
        context= {'form': form, 'id': id}  
        messages.success(request, 'Contacto actualizado.') 
        return render(request, 'contactos/edit.html', context)

def create(request):
    if request.method=='GET':
       form = ContactoForm()
       context= {'form': form}
       return render(request, 'contactos/create.html', context)
    
    if request.method=='POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('contactos')

def delete(request, id):
    contacto= Contacto.objects.get(id=id)
    contacto.delete()
    return redirect('contactos')
   
   
      