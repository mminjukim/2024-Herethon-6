from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from .models import Profile

def signup_view(request):
    if request.method == "GET":
        user_form = SignUpForm()
        return render(request, 'accounts/signup.html', {'user_form': user_form})
    
    user_form = SignUpForm(request.POST)
    
    if user_form.is_valid():
        user = user_form.save()
        login(request, user)
        return redirect('accounts:profile')  # main 앱의 main 페이지로 리디렉션
    else:
        return render(request, 'accounts/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def profile_view(request):
    if request.method == "GET":
        profile_form = ProfileForm()
        return render(request, 'accounts/profile.html', {'profile_form': profile_form})
    
    profile_form = ProfileForm(request.POST, request.FILES)
    
    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('main:main')  # main 앱의 main 페이지로 리디렉션
    else:
        return render(request, 'accounts/profile.html', {'profile_form': profile_form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

