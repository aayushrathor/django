from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetails(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
