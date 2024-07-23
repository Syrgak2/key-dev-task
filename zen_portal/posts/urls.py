from django.urls import path
from .views import PostListView, PostDetailView, CommentListView, RatingCreateView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post-list'),
    path('post_add/', PostListView.as_view(), name='post-add'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/comment/', CommentListView.as_view(), name='comment-list'),
    path('post/<int:post_id>/comment_add/', CommentListView.as_view(), name='comment-add'),
    path('post/<int:post_id>/mark_add/', RatingCreateView.as_view(), name='rating-add'),
]