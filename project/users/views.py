from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, logout


def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('app:index')
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    form = SignInForm(data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('app:index')
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign-in')
