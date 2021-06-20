from django.shortcuts import render
from django.views.generic import ListView, DetailView
from api.models import Post


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('-id')
    #context_object_name = 'posts'

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'    