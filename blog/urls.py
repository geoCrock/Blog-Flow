from django.urls import path
from .views import post_list, create_post, edit_post, delete_post, like_post, register, my_logout_view
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('create/', create_post, name='create_post'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', my_logout_view, name='my_logout_view'),
]
