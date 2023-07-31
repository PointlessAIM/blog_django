from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView
from .models import Post, PostView, Comment, Like, User
from .forms import BlogModelForm, CommentForm


class PostListView(ListView):
    model = Post
    
    
class PostDetailView(DetailView):
    model = Post
    def get_object(self, **kwargs):
        object=super().get_object(**kwargs)
        PostView.objects.get_or_create(user=self.request.user, post=object)
        return object
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment=form.instance
            comment.user=self.request.user
            comment.post=post
            comment.save()
            return redirect('entries:detail', slug=post.slug)
        return redirect('entries:detail', slug=self.get_object().slug)
        
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

class PostCreateView(CreateView):
    form_class = BlogModelForm
    model = Post
    success_url = '/'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Create'
        })
        return context
class PostUpdateView(UpdateView):
    form_class = BlogModelForm
    model = Post
    success_url = '/'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Update'
        })
        return context

class PostDeleteView(DeleteView):
    model = Post
    success_url='/'


def like(request, slug):
    user = request.user
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
    else:
        Like.objects.create(user=user, post=post)
    return redirect('entries:detail', slug=slug)





    
