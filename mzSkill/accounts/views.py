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
            request.session['usertype'] = request.POST['usertype'] # http 세션에 choice 데이터 저장해 다음 단계로 넘겨줌
            print(request.session['usertype'])
            return redirect(reverse('accounts:signup'))
        return render(request, 'rolechoice.html', {'form':form})
    

class SignUpView(View):  # 2단계 : 회원가입 
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            usertype = request.session.get('usertype')  # 세션에서 usertype 가져오기
            print(usertype)
            if usertype == '1':
                Learner.objects.create(user=user)
            elif usertype == '2':
                Teacher.objects.create(user=user)
            request.session['usertype'] = usertype # http 세션에 choice 데이터 저장해 다음 단계로 넘겨줌
            return redirect(reverse('accounts:writeprofile'))
        return render(request, 'signup.html', {'form': form})



class WriteProfileView(View): # 3단계 : 프로필 등록 

    def get(self, request, *args, **kwargs):
        if request.session['usertype'] == '1':
            print('러너가입됨')
            form = WriteLearnerProfileForm()
        else:
            print('티쳐가입됨')
            form = WriteTeacherProfileForm()
        return render(request, 'writeprofile.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        if request.session['usertype'] == '1':
            form = WriteLearnerProfileForm(request.POST, request.FILES)
            profile_model = Learner # 추가
        else:
            form = WriteTeacherProfileForm(request.POST, request.FILES)
            profile_model = Teacher # 추가

        if form.is_valid():
            user = request.user # 추가: 이미 존재하는 프로필 확인
            try:
                profile = profile_model.objects.get(user=user)
                form = form.save(commit=False)
                form.user = user
                form.id = profile.id  # 기존 프로필을 업데이트하도록 ID를 설정
                form.save()

            except profile_model.DoesNotExist:
                profile = form.save(commit=False)
                profile.user = user
                profile.save()

            request.session['usertype'] = request.session['usertype']
            return redirect(reverse('accounts:writedetails'))
        return render(request, 'writeprofile.html', {'form': form})

    

class WriteDetailsView(View): 

    def get(self, request, *args, **kwargs):
        if request.session['usertype'] == '1':
            return render(request, 'writedetails_learner.html')
        else:
            return render(request, 'writedetails_teacher.html')
    
    def post(self, request, *args, **kwargs):
        print(request.session['usertype'])
        if request.session['usertype'] == '1':
            profile = Learner.objects.get(user_id = request.user.id)
            # form = LearnerDetailsForm(request.POST, instance=profile)
            # if form.is_valid():
            #     id = profile.id
            #     form.save()
            #     return redirect('matching:match_teacher_list', id)
            # return render(request, 'writedetails_learner.html', {'form':form})
            id = profile.id
            skills = request.POST.getlist('skills[]')
            profile.skills.set(skills)
            personalities = request.POST.getlist('personalities[]')
            profile.personalities.set(personalities)
            return redirect('matching:match_teacher_list', id)
        else:
            profile = Teacher.objects.get(user_id = request.user.id)
            # form = TeacherDetailsForm(request.POST, instance=profile)
            # if form.is_valid():
            #     id = profile.id
            #     form.save()
            #     return redirect('accounts:teacher_registered', id)
            id = profile.id
            skills = request.POST.getlist('skills[]')
            profile.skills.set(skills)
            personalities = request.POST.getlist('personalities[]')
            profile.personalities.set(personalities)
            return redirect('accounts:teacher_registered', id)
    

def teacher_registered(request, id):
    profile = Teacher.objects.get(id = id)
    return render(request, 'teacher_registered.html', {'profile':profile})



# 로그인/로그아웃
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:main')
        else:
            error = "아이디 또는 비밀번호가 잘못되었습니다."
            return render(request, 'login.html', {'form': form, 'error':error})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
