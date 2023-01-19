from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': RegisterUserForm})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('todo:currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': RegisterUserForm,
                               'error': "That username has already been taken. Please Choose a new username."},
                              )
        else:
            # Tell the user the passwords didn't match
            return render(request, 'todo/signupuser.html',
                          {'form': RegisterUserForm, 'error': "Passwords didn't match"})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': LoginUserForm})
    else:
        # Login user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html',
                          {'form': LoginUserForm, 'error': "Username and password didn't match"})
        else:
            login(request, user)
            return redirect('todo:currenttodos')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todo:home')
