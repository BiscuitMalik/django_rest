from django.shortcuts import render
from rest_framework import generics, permissions # new
from .models import Post
from .serializers import PostSerializer

# Create your views here.
# posts/views.py
class PostList(generics.ListCreateAPIView): 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer