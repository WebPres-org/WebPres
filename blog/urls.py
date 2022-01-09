from . import views
from django.urls import path
from apps.user import views as user_views
from django.views.generic import ListView, DetailView
from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/index/', HomeView.as_view(), name='index'),
    #path('<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
    #path('add_post/', views.AddPostView.as_view(),  name='add_post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]