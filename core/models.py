from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    """Model representing a post"""

    # title of post
    title = models.CharField(max_length=250)

    # author of post - should we call user author because of default Django User model. 
    # maybe create Author model and establish Author - User 1:1 relationship
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name="posts")

    # text content of post
    content = models.TextField(max_length=1000)

    # URL link
    url = models.URLField(max_length=255)

    # date and time of post
    date_added = models.DateTimeField(auto_now_add=True)

    favorited_by = models.ManyToManyField('Author', related_name="favorite_posts")
    
    # adjusting the ordering so most recent is on top
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representing a author who can comment and write content"""
    # name of author
    name = models.CharField(max_length=100)

    # posts - is this necessary? Not in Local Library. Would probably only need the titles of the posts
    # post = models.CharField(max_length=250)

    # comments - same question, is this necessary?
    # comment = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Comment(models.Model):

    # author posting a comment. one to many
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, related_name="comments", null=True)

    # text of comment
    content = models.TextField(max_length=500)

    # date and time of post
    comment_date_added = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")

    favorited_by = models.ManyToManyField(Author, related_name="favorite_comments")

    class Meta:
        ordering = ['comment_date_added']

    def __str__(self):
        return self.content

