from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import BlogModelForm, BlogForm


def dummy_view(request):
    now = datetime.datetime.now()
    html = f"<html><body>time now: {now}, and id {id}</body></html>"
    return HttpResponse(html)

def status_code_view(request, exception = None):
    return HttpResponseNotFound('<h1>404: Page not found</h1>')

def entry_list(request):
    entries = Post.objects.all()
    blog_list = Post.objects.all()
    context = {
        'post_list': entries,
        'blog_list': blog_list
    }
    return render(request, 'posts/post_list.html', context) # request, template path, context

def redirect_home(request):
    return redirect('entries:entry-detail', id=1) # you can also redirect directly to '/entries/1'

class EntryFormView(FormView):
    template_name = 'form.html'
    form_class = BlogModelForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EntryClassDetailView(DetailView):
    model = Post

    def get_object(self):
        obj = super().get_object()
        return obj

class EntryListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_variable'] = "buenos días por la noche"
        return context
    
    def get_queryset(self):
        return Post.objects.all()[:1]

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

    
