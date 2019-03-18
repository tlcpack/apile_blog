from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    """Model representing a user post"""

    # title of post
    title = models.CharField(max_length=250)

    # author of post - User - ForeignKey relationship. does it go here?

    # text body of post
    body = models.TextField(max_length=1000)

    # URL link
    url = models.URLField(max_length=255)

    # date and time of post
    date = models.DateTimeField(auto_now_add=True)
    
    # adjusting the ordering so most recent is on top
    class Meta:
        ordering = ['-date']