from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='user-detail'),
    path('post/<int:post_pk>/favorite/', views.post_favorite_view, name = 'post_favorite'),
]