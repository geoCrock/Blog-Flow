from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like
from .forms import PostForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


@login_required(login_url='/register/')
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
    post = get_object_or_404(Post, id=post_id)

    if request.user.username != post.author:
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user.username != post.author:
        return redirect('post_list')

    post.delete()
    return redirect('post_list')


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    existing_like = Like.objects.filter(post=post, user=user).first()

    if existing_like:
        existing_like.delete()
    else:
        Like.objects.create(post=post, user=user)

    return redirect('post_list')


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


def my_logout_view(request):
    logout(request)
    return redirect('post_list')
