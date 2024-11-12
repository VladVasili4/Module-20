from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()      # Сохраняем нового пользователя
            login(request, user)      # Авторизуем пользователя сразу после регистрации
            return redirect('home')   # Перенаправляем на главную страницу
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    title = 'Home'
    context = {
        'title': title,
    }
    return render(request, 'home.html', context)


def users_list(request):
    users = CustomUser.objects.all()    # Извлекаем все записи из модели UserProfile
    return render(request, 'users_list.html', {'users': users})