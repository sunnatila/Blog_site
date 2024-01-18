from django.urls import path

from blog.views import (
    ArticleListView,
    ArticleDetailView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('post/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name='create_comment'),
]

