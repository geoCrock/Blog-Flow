from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import JsonResponse
from .forms import PostForm, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return JsonResponse({'success': True})


def increase_likes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'success': True})


def decrease_likes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes -= 1
    post.save()
    return JsonResponse({'success': True})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
