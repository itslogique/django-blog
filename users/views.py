from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
  """Handle users registration"""
  form = UserCreationForm()
  return render(request, 'users/register.html', {'form': form})


def login(request):
  """Handles users login"""
  form = AuthenticationForm()
  return render(request, 'users/login.html', {'form': form})
