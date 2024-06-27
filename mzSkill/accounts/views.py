from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def list(request):
    users = User.objects.all().order_by('-id')
    return render(request, "accounts/list.html", {'users': users })

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form' : form})
    
    form = SignUpForm(request.POST)

    if form.is_valid():
        user = form.save()
        return redirect('accounts:list')
    else:
        #여전히 회원가입 폼에 머물게 함
        return render(request, 'accounts/signup.html', {'form' : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('accounts:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:list')
