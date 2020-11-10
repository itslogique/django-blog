from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
  """Handle users registration"""
  if request.method == "POST":
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}')
      return redirect('blog-home')
  else:
    form = UserRegistrationForm()
  return render(request, 'users/register.html', {'form': form})


def login(request):
  """Handles users login"""
  form = AuthenticationForm()
  return render(request, 'users/login.html', {'form': form})
