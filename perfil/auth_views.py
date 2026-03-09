from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import constants


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['role'] = 'admin' if user.is_staff else 'user'
            messages.add_message(request, constants.SUCCESS, f'Bem-vindo, {user.username}!')
            next_url = request.GET.get('next', '/perfil/home/')
            return redirect(next_url)
        else:
            messages.add_message(request, constants.ERROR, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, 'Sessão encerrada com sucesso.')
    return redirect('landing')
