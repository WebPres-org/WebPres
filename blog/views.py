
from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required





@login_required(login_url='/login/')
class AddPostView(generic.CreateView):
    model = Post
    template_name = 'posts/add_post.html'
    fields = '__all__'


class PostList(generic.CreateView):
    model = Post
    template_name = 'posts/index.html'
    fields = '__all__'


class PostDetail(generic.CreateView):
    model = Post
    template_name = 'posts/post_detail.html'
    fields = '__all__'