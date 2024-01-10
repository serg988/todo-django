from django.shortcuts import render
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {"todo_list": todos})
