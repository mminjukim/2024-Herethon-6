from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse # 세션 구성에 필요
from django.views import View
from .forms import *
from .models import Profile


# 회원가입을 단계별로 구성하기 위해, 장고 세션 이용
# 참고1: https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Sessions
# 참고2: https://jupiny.com/2017/11/25/step-by-step-page-using-django-session/ (구버전 장고 주의)

class RoleChoiceView(View): # 1단계 : 역할 선택 (러너/티쳐)

    def get(self, request, *args, **kwargs):
        form = RoleChoiceForm()
        return render(request, 'accounts/rolechoice.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RoleChoiceForm(request.POST)
        if form.is_valid():
            request.session['role'] = form.data['choice'] # http 세션에 choice 데이터 저장해 다음 단계로 넘겨줌
            return redirect(reverse('accounts:signup'))
        return render(request, 'accounts/rolechoice.html', {'form':form})


class SignUpView(View): # 2단계 : 회원가입 

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['role'] = request.session['role']
            return redirect(reverse('accounts:profile'))
        return render(request, 'accounts/signup.html', {'form':form})


class ProfileView(View): # 3단계 : 프로필 등록 

    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'accounts/profile.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # profile = form.save(commit=False)
            # profile.role = request.session['role'] # 세션에 저장돼있던 role 정보를 현재 프로필의 role에 저장
            # profile.user = request.user
            # profile.save()
            request.session['nickname'] = form.data['nickname']
            request.session['birthDate'] = form.data['birthDate']
            request.session['profile_emoji'] = form.data['profile_emoji']
            request.session['role'] = request.session['role']
            return redirect(reverse('accounts:detail'))
        return render(request, 'accounts/profile.html', {'form':form})
    

class DetailView(View): # 4단계 : 프로필 세부사항 설정 

    def get(self, request, *args, **kwargs):
        form = DetailForm()
        return render(request, 'accounts/detail.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = DetailForm(request.POST)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user_id = request.user.id
            profile.nickname = request.session['nickname']
            profile.birthDate = request.session['birthDate']
            profile.profile_emoji = request.session['profile_emoji']
            profile.role = request.session['role'] 
            profile = form.save(commit = True)
            return redirect(reverse('main:main')) # 회원가입-프로필-세부설정까지 끝, 메인으로 
        
        return render(request, 'accounts/detail.html', {'form':form})


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

