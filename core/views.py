from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Post, Author
from .forms import CommentForm

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
    model = Author

def comment_new(request):
    form = CommentForm()
    return render(request, '/comment_new.html', {'form':form})