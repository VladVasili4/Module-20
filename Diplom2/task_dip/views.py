from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import UserRegistrationForm, PhotoForm, CommentForm
from .models import CustomUser, Photo, Comment
from django.contrib.auth.decorators import login_required



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




@login_required
def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'photo_gallery.html', {'photos': photos})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_gallery')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

@login_required
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    comments = photo.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo
            comment.user = request.user
            comment.save()
            return redirect('photo_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'photo_detail.html', {'photo': photo, 'comments': comments, 'form': form})
