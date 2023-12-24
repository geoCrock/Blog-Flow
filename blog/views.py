from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import JsonResponse


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(author=author, title=title, content=content)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.author = request.POST['author']
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


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
