from .auth_views import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'todo/home.html')


@login_required
def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', context={'form': CreateTodoForm()})
    else:
        try:
            form = CreateTodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('todo:currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html',
                          context={'form': CreateTodoForm(), 'error': 'Bad data passed in'})


@login_required
def current_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'todo/currenttodos.html', context={'todos': todos})


@login_required
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completedtodos.html', {'todos': todos})


@login_required
def view_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = CreateTodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = CreateTodoForm(request.POST, instance=todo)
            form.save()
            return redirect('todo:currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Bad info'})


@login_required
def complete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        if todo.date_completed is None:
            todo.date_completed = timezone.now()
        else:
            todo.date_completed = None
        todo.save()
        return redirect('todo:currenttodos')


@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:currenttodos')
