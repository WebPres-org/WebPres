from . import views
from django.urls import path
from .views import blog, search, CategoryView, blogdetail
from .views import PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    #New Setting
    path('post/', blog.as_view(), name="blog"),
    path('search', search, name="search"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('<slug:slug>/send-comment', views.send_comment, name="send_comment"),
    path('<slug:slug>/', blogdetail.as_view(), name="blog-detail"),
]





