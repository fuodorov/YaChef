from django.contrib.auth import get_user_model
from django.db import models

from .settings import *

User = get_user_model()


class Group(models.Model):
    title = models.CharField(GROUP_TITLE_VERBOUSE_NAME, max_length=GROUP_TITLE_MAX_LEN,
                             help_text=GROUP_TITLE_HELP_TEXT)
    slug = models.SlugField(GROUP_SLUG_VERBOUSE_NAME, max_length=GROUP_SLUG_MAX_LEN, unique=True,
                            help_text=GROUP_SLUG_HELP_TEXT)
    description = models.TextField(GROUP_DESCRIPTION_VERBOUSE_NAME, help_text=GROUP_DESCRIPTION_HELP_TEXT)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(POST_TEXT_VERBOUSE_NAME, help_text=POST_TEXT_VERBOUSE_NAME)
    pub_date = models.DateTimeField(POST_PUB_DATE_VERBOUSE_NAME, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=POST_RELATED_NAME,
                               verbose_name=POST_AUTHOR_VERBOUSE_NAME, help_text=POST_AUTHOR_HELP_TEXT)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, related_name=POST_RELATED_NAME,
                              verbose_name=POST_GROUP_VERBOUSE_NAME, help_text=POST_GROUP_HELP_TEXT )
    image = models.ImageField(upload_to=POST_IMAGE_UPLOAD_TO, blank=True, null=True,
                              verbose_name=POST_IMAGE_UPLOAD_TO, help_text=POST_IMAGE_HELP_TEXT)

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.text[:LETTERS_PER_STR]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name=COMMENT_RELATED_NAME,
                             verbose_name=COMMENT_POST_VERBOUSE_NAME, help_text=COMMENT_POST_HELP_TEXT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=COMMENT_RELATED_NAME,
                               verbose_name=COMMENT_AUTHOR_VERBOUSE_NAME, help_text=COMMENT_AUTHOR_HELP_TEXT)
    text = models.TextField(COMMENT_TEXT_VERBOUSE_NAME, help_text=COMMENT_TEXT_HELP_TEXT)
    created = models.DateTimeField(COMMENT_CREATED_VERBOUSE_NAME, auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.text[:LETTERS_PER_STR]


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=FOLLOW_USER_RELATED_NAME,
                             verbose_name=FOLLOW_USER_VERBOUSE_NAME, help_text=FOLLOW_USER_HELP_TEXT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=FOLLOW_AUTHOR_RELATED_NAME,
                               verbose_name=FOLLOW_AUTHOR_VERBOUSE_NAME, help_text=FOLLOW_AUTHOR_HELP_TEXT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'author'), name='follow_pair')]
