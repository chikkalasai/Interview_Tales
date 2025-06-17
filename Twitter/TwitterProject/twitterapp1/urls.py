from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import (
    RegisterViewSet, ProfileViewSet, PostViewSet, CommentViewSet, LikeViewSet,
)

router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')
router.register('profiles', ProfileViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

from .views import CreateCommentView,PostCommentsListView

urlpatterns = [
    path('api/', include(router.urls)),
    path('userdata/',views.userdatasender),
    path('updateprofileinfo/<int:pk>/',views.update_profile_info),
    path('getpostapi/<int:pk>/',views.getpostapi),
    path('deletepostapi/<int:pk>/',views.delete_post),
    path('api/comments/', CreateCommentView.as_view()), 
    path('api/posts/<int:post_id>/comments/', PostCommentsListView.as_view()),

]