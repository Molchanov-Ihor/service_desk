from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def user_login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('tickets:tickets-list')

    if request.method == 'GET':
        return render(request, 'registration/login.html', context=context)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets:tickets-list')
        else:
            context = {'error_message': 'Не корректний логін або пароль.'}
    return render(request, 'registration/login.html', context)


def user_logout(request):
    if request.user.is_authenticated:
        messages.success(request, 'Ви успішно розлогінились !')

    logout(request)
    return redirect('users:login')
