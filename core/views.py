from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from django.views import generic
from .models import Post

class Index(generic.ListView):
    """
    Generic class-based view for a list of all posts.
    """
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    """
    Generic detail view for a post
    """
    model = Post

class AuthorDetailView(generic.DetailView):
    """
    Generic detail view for an author
    """
    model = User