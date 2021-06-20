from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from api.models import Post


class IndexView(LoginRequiredMixin, ListView): 
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('-id')

class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'article_detail.html'    