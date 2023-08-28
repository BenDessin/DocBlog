from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/liste.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        #vérifie la requête en cour
        if self.request.user.is_authenticated:
            return queryset
        
        return queryset.filter(published = True)

#restreindre l'accès
@method_decorator(login_required, name='dispatch')
class BlogCreate(CreateView):
    model = BlogPost
    template_name = "blog/createBlog.html"
    fields = ['title', 'content',]
    
class BlogUpdate(UpdateView):
    model = BlogPost
    template_name = 'blog/UpdateBlog.html'
    fields = ['title', 'content', 'published']

class BlogDetail(DetailView):
    model = BlogPost
    context_object_name = "posts"
    
class BlogDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts:Home')
    context_object_name = "posts"