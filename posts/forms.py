from django.forms import ModelForm

from .models import Comment, Post
from .settings import POST_FORM_FIELDS, POST_COMMENT_FIELDS


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = POST_FORM_FIELDS


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = POST_COMMENT_FIELDS
