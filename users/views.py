from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request, *args, **kwargs):
    """Handle users registration"""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Your Account has been created successfully! you can now login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request, *args, **kwargs):
    """Handles users profile"""
    return render(request, 'users/profile.html')
