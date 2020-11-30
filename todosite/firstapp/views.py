from .forms import CreateUserForm
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

def RegisterUser(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.warning(request, 'An Account was made for ' + user)

				return redirect('/login')
			

		context = {'form':form}
		return render(request, 'firstapp/register.html', context)

def LoginUser(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Your username or your password is incorrect')

		context = {}
		return render(request, 'firstapp/login.html', context)

def LogoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def Home(request):
    return render(request, 'firstapp/home.html')

@login_required(login_url='login')
def ToDo(request):
    tasks = Task.objects.all()


    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/task')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'firstapp/task.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/task')

    context = {'form':form}

    return render(request, 'firstapp/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/task')

    context = {'item':item}
    return render(request, 'firstapp/delete_task.html', context)

@login_required(login_url='login')
def status(request):
    tasks = Task.objects.all()


    context = {'tasks':tasks}

    return render(request, 'firstapp/status.html', context)

@login_required(login_url='login')
def delete_all(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        tasks.delete()
        return redirect('/task')

    context = {'tasks':tasks}

    return render(request, 'firstapp/delete_all.html', context)

@login_required(login_url='login')
def aboutUs(request):
    return render(request, 'firstapp/about.html')

@login_required(login_url='login')
def Note(request, pk):

    item = Task.objects.get(id=pk)

    form = TaskForm(instance=item)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/task')

    context = {'item':item, 'form':form}

    return render(request, 'firstapp/note.html', context)

@login_required(login_url='login')
def priority(request):
    tasks = Task.objects.all()

    context = {'tasks':tasks}

    return render(request, 'firstapp/prior.html', context)


