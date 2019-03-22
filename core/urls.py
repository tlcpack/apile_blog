from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='user-detail'),
    path('post/<int:pk>/favorite/', views.post_favorite_view, name='post_favorite'),
    path('post/<int:pk>/comment_new/', views.comment_new, name='comment_new'),
    path('comment/<int:pk>', views.comment_favorite_view, name='comment_favorite')
]