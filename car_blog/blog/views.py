from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Category, Element
from .serializers import PostSerializer, CategorySerializer

class LatestPosts(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[0:5]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_cat_obj(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_cat_obj(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class PostDetail(APIView):
    def get_post_obj(self, category_slug, post_slug):
        try:
            return Post.objects.filter(category__slug=category_slug).get(slug=post_slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, post_slug, format=None):
        post = self.get_post_obj(category_slug, post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
