from django.shortcuts import render
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


def about(request, *args, **kwargs):
  """About page for blog"""
  return render(request, 'blog/about.html', {'title': 'About'})
