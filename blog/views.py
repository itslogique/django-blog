from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


posts = [
    {
        'author': 'Ujah Emmanuel',
        'title': 'Django Custom User Model',
        'content': 'In this article we will learn how to create a Django Custom User Model by extending AbstractBaseUser class and the BaseUserManager...',
        'date_posted': '09th November, 2020'
    },
    {
        'author': 'Ujah Emmanuel',
        'title': 'Build a REST API with DRF',
        'content': 'In this article we will learn how to build a REST API with Django Rest Framework',
        'date_posted': '09th November, 2020'
    }
]


def home(request, *args, **kwargs):
  """Blog home page"""
  context = {
      'posts': Post.objects.all(),
      'title': 'blog-home'
  }
  return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request, *args, **kwargs):
  """About page for blog"""
  return render(request, 'blog/about.html', {'title': 'About'})
