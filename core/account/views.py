from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            messages.success(request, 'Вы вошли в аккаунт')
            login(request, user)

            return redirect('index_path')
        else:
            messages.error(request, 'Что-то пошло не так')
            return redirect('login_path')
    else:
        login_form = LoginForm()

    content = {
        'login_form': login_form,
        'title': 'Вход в аккаунт'
    }
    return render(request, 'account/login.html', content)


def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login_path')
        else:
            messages.error(request, 'Что-то пошло не так')
            return redirect('register_path')
    else:
        register_form = RegisterForm()

    content = {
        'register_form': register_form,
        'title': 'Регистрация'
    }
    return render(request, 'account/register.html', content)


def logout_view(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('index_path')
