from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from forum.forms import NewThreadForm, PostForm
from forum.models import Category, Forum_Thread, Post


def start(request):
    return render(request, '')


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def category_threads(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'threads.html', {'category': category})


@login_required
def new_thread(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = NewThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.owner = request.user
            thread.save()

            Post.objects.create(
                content=form.cleaned_data.get('message'),
                forum_thread=thread,
                owner=request.user,
            )
            return redirect('thread_posts', pk=pk, thread_pk=thread.pk)

    else:
        form = NewThreadForm()

    return render(request, 'new_thread.html', {'category': category, 'form': form})


def thread_posts(request, pk, thread_pk):
    thread = get_object_or_404(Forum_Thread, category__pk=pk, pk=thread_pk)
    thread.views += 1
    thread.save()
    return render(request, 'thread_posts.html', {'thread': thread})


@login_required
def reply_thread(request, pk, thread_pk):
    thread = get_object_or_404(Forum_Thread, category__pk=pk, pk=thread_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.forum_thread = thread
            post.owner = request.user
            post.save()
            return redirect('thread_posts', pk=pk, thread_pk=thread_pk)
    else:
        form = PostForm()
    return render(request, 'reply_thread.html', {'thread': thread, 'form': form})
