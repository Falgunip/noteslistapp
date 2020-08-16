from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST) #Pass Post method
        if form.is_valid():
            form.save() #Saves to the database
        return redirect('/') #Send back to same url path

    context = {'tasks' : tasks,'form':form}
    return render(request,'tasks/list.html',context) #This will return the template just created

def updateTask(request,pk): #pk is a url pattern. pk = primary key
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) #need 'instance=' because if not then it will make a new instance
        if form.is_valid():
            form.save()
        return redirect('/') #redirect back to homepage

    context = {'form': form}
    return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)



