from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView
from .models import Post, PostView, Comment, Like, User
from .forms import BlogModelForm, BlogForm


class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post    

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'thumbnail', 'author', 'slug')

class PostDeleteView(DeleteView):
    model = Post
    success_url='/'


class EntryFormView(FormView):
    template_name = 'blog_form.html'
    form_class = BlogModelForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def post_create(request):
    # form = BlogForm(request.POST or None)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     name=form.cleaned_data.get("name")
    #     tagline=form.cleaned_data.get("tagline")
    #     blog = Blog(name=name, tagline=tagline)
    #     blog.save()
    #     return redirect("entries:entry-list")
    # context = {
    #     "form": form
    # }
    form = BlogModelForm(request.POST or None, request.FILES or None)# if you dont add the second half, you cant upload images
    if form.is_valid():
        form.save()
        return redirect("entries:entry-list")
    context = {
        "form": form
    }
    return render(request, "form.html", context)

    
