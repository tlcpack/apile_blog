from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    """Model representing a user post"""

    # title of post
    title = models.CharField(max_length=250)

    # user/author of post
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    # text content of post
    content = models.TextField(max_length=1000)

    # URL link
    url = models.URLField(max_length=255)

    # date and time of post
    date_added = models.DateTimeField(auto_now_add=True)

    # comment field - may not be necessary here
    # comment = models.ManyToManyField(Comment, null=True, blank=True, help_text="What do you think about this post?")
    # comment = models.ForeignKey('Comment', on_delete=SET_NULL, null=True, help_text="What do you think about this post?")

    # votes - may not be necessary here
    # vote_by = models.ManyToManyField(to=User, through='Vote')
    
    # adjusting the ordering so most recent is on top
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class User(models.Model):
    """Model representing a user who can comment and write content"""
    # name of user
    name = models.CharField(max_length=100)

    # posts - is this necessary? Not in Local Library. Would probably only need the titles of the posts
    # post = models.CharField(max_length=250)

    # comments - same question, is this necessary?
    # comment = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Comment(models.Model):

    # user posting a comment. one to many
    user = models.ForeignKey('User', on_delete=models.SET_NULL)

    # text of comment
    content = models.TextField(max_length=500)

    # date and time of post
    comment_date_added = models.DateTimeField(auto_now_add=True)

    vote = models.ForeignKey('Vote', on_delete=models.SET_NULL, related_name="votes")

    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-comment_date_added']

    def __str__(self):
        return self.description

class Vote(models.Model):

    # user voting. one to many
    user = models.ForeignKey('User', on_delete=models.SET_NULL)

    post = models.ForeignKey('Post', on_delete=models.CASCADE)