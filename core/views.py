from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods



# Create your views here.

from django.views import generic
from .models import Post, Comment
from django.db.models import Count, F
from .forms import CommentForm, PostForm

class Index(generic.ListView):
    """
    Generic class-based view for a list of all posts.
    """
    model = Post
    paginate_by = 5
    queryset = Post.objects.all()

    def get_queryset(self):
        """
        This function changes the set of data that is retrieved from 
        the database by looking at the get parameters.
        """
        self.sort = self.request.GET.get('sort')
        post_list=self.queryset
        post_list=post_list.annotate(favorites=Count('favorited_by'))

        if self.sort in ['favorites', 'date_added']:
            post_list=post_list.order_by(F(self.sort).desc(nulls_last=True))

        return post_list

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


@require_http_methods(['POST'])
@login_required
def post_favorite_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # We want to toggle whether this post is favorited.
    # If we find a favorite with this user and post (i.e. it is not created
    # prior to this moment) then delete that favorite, otherwise create it.
    
    if post in request.user.favorite_posts.all():
        request.user.favorite_posts.remove(post)
    else:
        request.user.favorite_posts.add(post)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_http_methods(['POST'])
@login_required
def comment_favorite_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # We want to toggle whether this comment is favorited.
    # If we find a favorite with this user and comment (i.e. it is not created
    # prior to this moment) then delete that favorite, otherwise create it.
    
    if comment in request.user.favorite_comments.all():
        request.user.favorite_comments.remove(comment)
    else:
        request.user.favorite_comments.add(comment)

    return redirect(request.META.get('HTTP_REFERER', '/'))

# form page for creating a post
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

# form page for submitting comment
@login_required
def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_new.html', {'form':form, 'post':post})

