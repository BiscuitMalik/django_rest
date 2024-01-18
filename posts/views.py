# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,) # it must be in tuple so we need add ',' in the add
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
