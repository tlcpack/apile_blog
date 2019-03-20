from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('core/post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('core/author/<int:pk>', views.AuthorDetailView.as_view(), name='user-detail'),
]