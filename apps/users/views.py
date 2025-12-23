from apps.users.forms import UserForm
from apps.users.models import Position
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
    logout(request)
    return redirect('users:login')


def user_registration(request):
    if request.user.is_authenticated:
        return redirect('tickets:tickets-list')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.position = Position.objects.filter(id=1).first()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('tickets:tickets-list')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})
