from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm, UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user
            obj.save()
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Data!')
            return redirect('home')

    context = {'tasks' : tasks}
    return render(request, 'task/home.html', context)


def delete_task(request, pk):
    obj = Task.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    
    return render(request, 'task/delete_task.html', {'obj': obj})


def edit_task(request, pk):
    obj = Task.objects.get(id=pk)
    obj.name = request.user
    form = TaskForm(instance=obj)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'task/edit_task.html', context)


def create_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'User created for name %s' % username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username or Password did not matched!')
            
    context = {}
    return render(request, 'registration/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_profile(request):
    
    page = 'profile'
    
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'task/profile.html')