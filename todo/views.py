from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    context = { "todos": todos}
    return render(request, 'todo/index.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successfully')
            return redirect('index')
        else:
            messages.error(request, 'Error creating todo')
            return render(request, 'todo/create-todo.html', { "form": form })
    else:
        form = TodoForm()
        context = { "form": form }
        return render(request, 'todo/create-todo.html', context)
        

def edit_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully')
            return redirect('index')
        else:
            messages.error(request, 'Error updating todo')
            return render(request, 'todo/create-todo.html', { "form": form })
    else:
        form = TodoForm(instance=todo)
        context = { "form": form }
        return render(request, 'todo/create-todo.html', context)


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('index')

def complete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    messages.success(request, 'Todo updated successfully')
    return redirect('index')
