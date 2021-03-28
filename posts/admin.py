from django.contrib.admin import ModelAdmin, register

from .models import Comment, Follow, Group, Post

@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'image')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('pk', 'post', 'text', 'author', 'created')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


@register(Follow)
class FollowAdmin(ModelAdmin):
    list_display = ('pk', 'author', 'user')
    list_filter = ('author', 'user')
