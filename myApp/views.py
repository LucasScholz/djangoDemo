from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm


# Create your views here.


def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def add_todo(request):
    if (request.method == 'POST'):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TodoItemForm()
    return render(request, 'add_todo.html', {'form': form})


def toggle_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id =todo_id)
    if request.method == 'POST':
        todo.completed = "completed" in request.POST
        todo.save()
    return redirect("todos")