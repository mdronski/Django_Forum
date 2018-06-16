from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from forum.forms import NewThreadForm
from forum.models import Category, Forum_Thread, Post


def start(request):
    return render(request, '')


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def category_threads(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'threads.html', {'category': category})


def new_thread(request, pk):
    category = get_object_or_404(Category, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user

    if request.method == 'POST':
        form = NewThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.owner = user
            thread.save()

            post = Post.objects.create(
                content=form.cleaned_data.get('message'),
                thread=thread,
                owner=user
            )
            return redirect('category_threads', pk=category.pk)  # TODO: redirect to the created topic page

    else:
        form = NewThreadForm()

    return render(request, 'new_thread.html', {'category': category, 'form': form})
