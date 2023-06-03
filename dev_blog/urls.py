# from rest_framework import routers
from django.urls import path

from dev_blog.views import mongo_operations
# from dev_blog.views import BlogViewSet, PostViewSet

# router = routers.DefaultRouter()
urlpatterns = [
    path('mongo', mongo_operations)
]
# router.register(r'blog', BlogViewSet, basename='blog-list')
# router.register(r'post', PostViewSet, basename='post-list')
