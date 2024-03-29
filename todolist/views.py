from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {"todo_list": todos})


def new_todo(request):
    todo_title = request.POST['title']
    todo = Todo(title=todo_title)
    todo.save()
    return redirect('/')

def complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return HttpResponseRedirect("/")


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.is_completed:
        todo.delete()
    return HttpResponseRedirect("/")
