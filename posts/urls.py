from django.urls import path , include
from .views import *


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/', UserList.as_view()),
        
]