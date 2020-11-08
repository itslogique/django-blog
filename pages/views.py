from django.shortcuts import render


def landing(request, *args, **kwargs):
  """landing page for blog"""
  return render(request, 'pages/landing.html')


def about(request, *args, **kwargs):
  """About page for blog website"""
  return render(request, 'pages/about.html')
