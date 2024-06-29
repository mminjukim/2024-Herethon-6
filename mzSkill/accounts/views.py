from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse # 세션 구성에 필요

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import *


# 회원가입을 단계별로 구성하기 위해, 장고 세션 이용
# 참고1: https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Sessions
# 참고2: https://jupiny.com/2017/11/25/step-by-step-page-using-django-session/ (구버전 장고 주의)

class RoleChoiceView(View): # 1단계 : 역할 선택 (러너/티쳐)

    def get(self, request, *args, **kwargs):
        form = RoleChoiceForm()
        return render(request, 'rolechoice.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RoleChoiceForm(request.POST)
        if form.is_valid():
            request.session['usertype'] = form.data['usertype'] # http 세션에 choice 데이터 저장해 다음 단계로 넘겨줌
            return redirect(reverse('accounts:signup'))
        return render(request, 'rolechoice.html', {'form':form})
    

class SignUpView(View): # 2단계 : 회원가입 

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['usertype'] = request.session['usertype'] # http 세션에 choice 데이터 저장해 다음 단계로 넘겨줌
            return redirect(reverse('accounts:writeprofile'))
        return render(request, 'signup.html', {'form':form})


class WriteProfileView(View): # 3단계 : 프로필 등록 

    def get(self, request, *args, **kwargs):
        if request.session['usertype'] == 1:
            form = WriteLearnerProfileForm()
        else:
            form = WriteTeacherProfileForm()
        return render(request, 'writeprofile.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        if request.session['usertype'] == 1:
            form = WriteLearnerProfileForm(request.POST, request.FILES)
        else:
            form = WriteTeacherProfileForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['nickname'] = form.data['nickname']
            request.session['birthdate'] = form.data['birthdate']
            request.session['emoji'] = form.data['emoji']
            request.session['usertype'] = request.session['usertype'] # http 세션에 choice 데이터 저장해 다음 단계로 넘겨줌
            return redirect(reverse('accounts:writedetails'))
        return render(request, 'writeprofile.html', {'form':form})
    

class WriteDetailsView(View):

    def get(self, request, *args, **kwargs):
        if request.session['usertype'] == 1:
            form = LearnerDetailsForm(request.POST)
        else:
            form = TeacherDetailsForm(request.POST)
        return render(request, 'writedetails.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        if request.session['usertype'] == 1:
            form = LearnerDetailsForm(request.POST)
        else:
            form = TeacherDetailsForm(request.POST)

        if form.is_valid():
            profile = form.save(commit = False)
            profile.user_id = request.user.id
            profile.nickname = request.session['nickname']
            profile.birthdate = request.session['birthdate']
            profile.emoji = request.session['emoji']
            profile = form.save(commit = True)
            return redirect(reverse('main:main')) # 회원가입-프로필-세부설정까지 끝, 메인으로 

        return render(request, 'writedetails.html', {'form':form})
    


# 로그인/로그아웃

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
