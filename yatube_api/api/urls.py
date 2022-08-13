from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/'),
    path('api/v1/posts/'),
    path('api/v1/posts/<int:post_id>/'),
    path('api/v1/groups/'),
    path('api/v1/groups/<int:group_id>/'),
    path('api/v1/posts/<int:post_id>/comments/'),
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/'),
    path('', include(router.urls)),
]
