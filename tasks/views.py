from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, TaskList
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskList(request.POST)
        print("POST DATA:", request.POST)  # 👀 Check incoming data
        if form.is_valid():
            todo_list = form.save(commit=False)   # 👈 don’t save yet
            todo_list.user = request.user         # 👈 link to logged-in user
            todo_list.save()
            print("✅ Saved list:", todo_list)
        else:
            print("❌ Form errors:", form.errors)  # 👀 Show validation errors
        return redirect("tasks:home")

    form = TaskList()
    lists = ToDoList.objects.filter(user=request.user)  # 👈 only show their lists
    context = {"form": form, "lists": lists}

    return render(request, 'tasks/home.html', context)



def update_list(request, pk):
    todo_list = get_object_or_404(ToDoList, id=pk, user=request.user)  # 👈 secure
    form = TaskList(instance=todo_list)

    if request.method == 'POST':
        form = TaskList(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
        return redirect('tasks:home')

    context = {"form": form}
    return render(request, 'tasks/update_list.html', context)


def delete_list(request, pk):
    todo_list = get_object_or_404(ToDoList, id=pk, user=request.user)  # 👈 secure
    if request.method == 'POST':
        todo_list.delete()
        return redirect("tasks:home")
    context = {"list": todo_list}
    return render(request, 'tasks/delete_list.html', context)

###############################################################################

def task(request, pk):
    todo_list = get_object_or_404(ToDoList, id=pk, user=request.user)  # 👈 secure

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.todo_list = todo_list
            task.save()
        return redirect("tasks:tasks", pk=pk)

    form = TaskForm()
    tasks = todo_list.items.all()

    context = {
        "todo_list": todo_list,
        "tasks": tasks,
        "form": form,
    }
    return render(request, 'tasks/index.html', context)


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    todo_list = get_object_or_404(ToDoList, id=task.todo_list.id, user=request.user)  # 👈 secure
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks:tasks', pk=todo_list.id)

    context = {"task": task, 'form': form, "todo_list_id": todo_list.id}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    todo_list = get_object_or_404(ToDoList, id=task.todo_list.id, user=request.user)  # 👈 secure

    if request.method == 'POST':
        task.delete()
        return redirect("tasks:tasks", pk=todo_list.id)

    context = {"task": task, "todo_list_id": todo_list.id}
    return render(request, 'tasks/delete.html', context)
