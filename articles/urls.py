from django.urls import path

from articles.views import my_view, PostDetailView, AddPostView, CategoryPost, LikeView, UnLikeView, words_view

urlpatterns = [
    path('', my_view, name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/add', AddPostView.as_view(), name='add-post'),
    path('category/<int:pk>/posts/', CategoryPost.as_view(), name='category-post'),
    path('like/<int:pk>', LikeView.as_view(), name='like-posts'),
    path('unlike/<int:pk>', UnLikeView.as_view(), name='unlike-posts'),
    path('mysite', words_view),
]
