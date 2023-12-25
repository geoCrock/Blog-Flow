from django.urls import path
from .views import post_list, create_post, edit_post, delete_post, increase_likes, decrease_likes

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('like/increase/<int:post_id>/', increase_likes, name='increase_likes'),
    path('like/decrease/<int:post_id>/', decrease_likes, name='decrease_likes'),
    path('create/', create_post, name='create_post'),

]
