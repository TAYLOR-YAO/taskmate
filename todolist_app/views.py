from django.core import paginator
from django.shortcuts import render, redirect
from todolist_app.models import Tasklist
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# All Todo List views here.


def index(request):
    context = {
        'index_text': "Welcome To Home Page!",
    }
    return render(request, 'index.html', context)


@login_required
def todolist(request):
    # create task Post POST reqest Then Redirect user to the same page 'todolist'
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            # Adding the manager filed to the task form
            instance = form.save(commit=False)
            instance.manage = request.user
            # Then fave form
            instance.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        # all_tasks = Tasklist.objects.all()      this retieve all tasks
        # filter tasks by logged in user
        all_tasks = Tasklist.objects.filter(manage=request.user)
        # implement pagination to display 5 task per page
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


@login_required
def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restricted, you are not allowed!"))
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    # create task Post POST reqest Then Redirect user to the same page 'todolist'
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


@login_required
def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restricted, you are not allowed!"))
    return redirect('todolist')


@login_required
def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def contact(request):
    context = {
        'contact_text': "Our contacts page in design, visite us again shortly. Thanks for visiting us!",
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': "About us page in design, visite us again shortly. Thanks for visiting us!",
    }
    return render(request, 'about.html', context)
