from django.shortcuts import render, redirect
from .models import Post
from django.conf import settings
from django.http import HttpResponseNotFound
from .forms import *


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'students': ["Вася", "Петя", "Даня", "Маша"]
    }
    return render(request, 'index.html', context)


def about(request):

    context = {
        'title': 'О компании'
    }
    return render(request, 'about.html', context)


def contacts(request):

    context = {
        'title': 'Контакты'
    }
    return render(request, 'contacts.html', context)

# система аутенцификации

def post_detail(request, slug):
    post = Post.objects.filter(slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.post = post[0]
        instance.save()
        return redirect('app:post', slug=slug)
    if not post:
        return HttpResponseNotFound(
            'Такой страницы не существует'
        )

    post = post[0]
    return render(request, 'post.html', {'post': post, 'form': form})


def post_create(request):
    post_form = PostForm(request.POST)

    if request.method == 'POST' and post_form.is_valid():
        images = request.FILES.getlist('images')

        instance = post_form.save(commit=False)
        instance.author = request.user
        instance.save()

        for image in images:
            Photo.objects.create(post=instance, image=image)

        return redirect('app:index')

    post_form = PostForm()
    return render(request, 'post_create.html',
                  {'post_form': post_form})
