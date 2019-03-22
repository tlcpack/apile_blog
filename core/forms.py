from django import forms
from core.models import Post, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'url',)
        # may need to allow users a blank URL in case they are posting non-linking posts