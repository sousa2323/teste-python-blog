from django.shortcuts import render
from django.views.generic import ListView, DetailView
from api.views import postkList


class IndexView(ListView):
    model = postkList
    template_name = 'index.html'
    queryset = postkList.objects.all().order_by('-id')
    context_object_name = posts