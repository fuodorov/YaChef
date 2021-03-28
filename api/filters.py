from django_filters.rest_framework import FilterSet, CharFilter

from posts.models import Post


class GroupFilter(FilterSet):
    group = CharFilter(lookup_expr='exact')

    class Meta:
        model = Post
        fields = ('group',)
