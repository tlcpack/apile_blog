from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """Model representing a post"""

    # title of post
    title = models.CharField(max_length=250)

    # author of post - should we call user author because of default Django User model. 
    # maybe create Author model and establish Author - User 1:1 relationship
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")

    # text content of post
    content = models.TextField(max_length=1000)

    # URL link
    url = models.URLField(max_length=255)

    # date and time of post
    date_added = models.DateTimeField(auto_now_add=True)

    favorited_by = models.ManyToManyField(User, related_name="favorite_posts")
    
    # adjusting the ordering so most recent is on top
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):

    # author posting a comment. one to many
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="comments", null=True)

    # text of comment
    content = models.TextField(max_length=500)

    # date and time of post
    comment_date_added = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")

    favorited_by = models.ManyToManyField(User, related_name="favorite_comments")

    class Meta:
        ordering = ['comment_date_added']

    def __str__(self):
        return self.content

