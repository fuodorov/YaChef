from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('follow', FollowViewSet, basename='FollowView')
v1_router.register('group', GroupViewSet, basename='GroupView')
v1_router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet, basename='CommentView')
v1_router.register('posts', PostViewSet, basename='PostView')

urlpatterns = [
    path('redoc/', TemplateView.as_view(template_name='redoc.html'), name='redoc'),
    path('v1/', include(v1_router.urls)),
]
