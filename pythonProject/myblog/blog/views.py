from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForms
from .models import Post


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Показывать по 5 записей на странице

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, отобразить первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, отобразить последнюю.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html',
                  {'posts': posts, 'is_paginated': True if posts.has_other_pages() else False})


def postview(request, pk):
    result = Post.objects.get(id=pk)
    data = {
        'result': result,
    }

    return render(request, 'blog/post.html', data)


def post_updateview(request, pk):
    post = Post.objects.get(id=pk)  # Получаем объект поста по id
    if request.method == 'POST':
        form = PostForms(request.POST, instance=post)  # Инициализируем форму с данными POST и экземпляром поста
        if form.is_valid():
            form.save()  # Сохраняем изменения в посте
            messages.success(request, "Публикация успешно обновлена!")
            return redirect('home')
        else:
            messages.error(request, "Ошибка заполнения")
    else:
        form = PostForms(instance=post)  # Инициализируем форму с экземпляром поста для отображения текущих данных

    return render(request, 'blog/post_update.html', {'form': form})


def post_deleteview(request, pk):
    post_to_delete = Post.objects.get(id=pk)
    post_to_delete.delete()
    messages.success(request, "Публикация успешно удалена!")

    return redirect('home')


def post_createview(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()  # Это сохранит объект Post, используя данные формы
            messages.success(request, "Публикация успешно добавлена!")
            return redirect('home')
        else:
            messages.error(request, "Ошибка заполнения")
    else:
        form = PostForms()

    return render(request, 'blog/post_create.html', {'form': form})