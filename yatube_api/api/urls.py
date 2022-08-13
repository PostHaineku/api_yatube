from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter() 

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/'), # передаём логин и пароль, получаем токен.
    path('api/v1/posts/'), # получаем список всех постов или создаём новый пост.
    path('api/v1/posts/<int:post_id>/'), # получаем, редактируем или удаляем пост по id.
    path('api/v1/groups/'), # получаем список всех групп.
    path('api/v1/groups/<int:group_id>/'), # получаем информацию о группе по id.
    path('api/v1/posts/<int:post_id>/comments/'), # получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/'), # (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
    path('', include(router.urls)),
]
