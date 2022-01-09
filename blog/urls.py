from . import views
from django.urls import path
from apps.user import views as user_views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
    #path('add_post/', views.AddPostView.as_view(),  name='add_post'),
]