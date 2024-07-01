from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View
from .forms import DetailForm, LearnerProfileForm, RoleChoiceForm, SignUpForm, TeacherProfileForm, TeachingPlanForm
from .models import LearnerProfile, Skill, TeacherProfile, TeachingPlan

# 역할 선택 뷰 : 폼 코드가 html폼의 구성과 맞지 않을 수도 있다. 그러면 view가 작동하더라도 폼이 렌더링 되지 않을 수도 있음.
class RoleChoiceView(View):
    def get(self, request, *args, **kwargs):
        form = RoleChoiceForm()
        return render(request, 'profiles/rolechoice.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RoleChoiceForm(request.POST)
        if form.is_valid():
            request.session['role'] = form.cleaned_data['choice']
            # 회원가입 창으로 넘어가기
            return redirect(reverse('profiles:signup'))
        return render(request, 'profiles/rolechoice.html', {'form': form})

# 회원가입 뷰
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'profiles/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            role = request.session.get('role')

            if role == '1':
                return redirect('profiles:profile_setup')
            elif role == '2':
                return redirect('profiles:profile_setup')
            else:
                print("Role is not set properly in session:", role)
                # 디버깅을 위해 세션의 내용을 출력합니다.
                print("Session data:", request.session.items())
        else:
            # 폼 에러를 콘솔에 출력하여 디버깅
            print("Form is not valid:", form.errors)

        return render(request, 'profiles/signup.html', {'form': form})


# 아이디 생성 후 프로필 세부사항 설정 뷰 >> 메인으로 넘어감
class ProfileSetupView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        role = request.session.get('role')
        if role == '1':
            form = LearnerProfileForm()
        elif role == '2':
            form = TeacherProfileForm()
        else:
            return redirect('profiles:role_choice')
        return render(request, 'profiles/profile_setup.html', {'form': form})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        role = request.session.get('role')
        if role == '1':
            form = LearnerProfileForm(request.POST, request.FILES)
        elif role == '2':
            form = TeacherProfileForm(request.POST, request.FILES)
        else:
            return redirect('profiles:role_choice')

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profiles:skill_selection')
        else:
            print("Profile setup form is not valid:", form.errors)

        return render(request, 'profiles/profile_setup.html', {'form': form})

    
# 스킬 선택 뷰
class SkillSelectionView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = DetailForm()
        return render(request, 'profiles/skill_selection.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = DetailForm(request.POST)
        if form.is_valid():
            skills = form.cleaned_data['skills']
            user = request.user
            role = request.session.get('role')
            if role == '1':
                profile = LearnerProfile.objects.get(user=user)
            else:
                profile = TeacherProfile.objects.get(user=user)
            profile.skills.set(skills)
            profile.save()

            form.save_m2m()

            return redirect('main:main')
        return render(request, 'profiles/skill_selection.html', {'form': form})


# 로그인 뷰
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:main')
    else:
        form = AuthenticationForm()
    return render(request, 'profiles/login.html', {'form': form})

# 러너 프로필 뷰
@login_required
def learner_profile_view(request, username):
    try:
        profile = LearnerProfile.objects.get(user__username=username)
    except LearnerProfile.DoesNotExist:
        profile = None

    return render(request, 'profiles/learner_profile.html', {'profile': profile})


# 티쳐 프로필 뷰
@login_required
def teacher_profile_view(request, username):
    try:
        profile = TeacherProfile.objects.get(user__username=username)
    except TeacherProfile.DoesNotExist:
        profile = None

    return render(request, 'profiles/teacher_profile.html', {'profile': profile})

# 러너 프로필 편집 뷰
@login_required
def learner_profile_edit_view(request):
    user = request.user
    try:
        profile = LearnerProfile.objects.get(user=user)
    except LearnerProfile.DoesNotExist:
        profile = None
    
    if request.method == "POST":
        form = LearnerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            learner_profile = form.save(commit=False)
            learner_profile.user = user
            learner_profile.save()

            # 스킨 필드를 명시적으로 업데이트한다.
            form.save_m2m()    

            return redirect('profiles:learner_profile', username=user.username)
    else:
        form = LearnerProfileForm(instance=profile)
    
    return render(request, 'profiles/learner_profile_edit.html', {'form': form})

# 티쳐 프로필 편집 뷰
@login_required
def teacher_profile_edit_view(request):
    user = request.user
    try:
        profile = TeacherProfile.objects.get(user=user)
    except TeacherProfile.DoesNotExist:
        profile = TeacherProfile(user=user)
    
    try:
        teaching_plan = TeachingPlan.objects.get(profile=profile)
    except TeachingPlan.DoesNotExist:
        teaching_plan = None

    if request.method == "POST":
        profile_form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        teaching_plan_form = TeachingPlanForm(request.POST, instance=teaching_plan)

        if profile_form.is_valid() and teaching_plan_form.is_valid():
            teacher_profile = profile_form.save(commit=False)
            teacher_profile.user = user
            teacher_profile.save()
            profile_form.save_m2m()  # ManyToMany 필드 저장
            
            teaching_plan = teaching_plan_form.save(commit=False)
            teaching_plan.profile = profile
            teaching_plan.save()

            return redirect('profiles:teacher_profile', username=user.username)
    else:
        profile_form = TeacherProfileForm(instance=profile)
        teaching_plan_form = TeachingPlanForm(instance=teaching_plan)
    
    return render(request, 'profiles/teacher_profile_edit.html', {
        'profile_form': profile_form,
        'teaching_plan_form': teaching_plan_form
    })


# 로그아웃 뷰
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('profiles:login')

# 프로필이 설정되지 않았을 경우
# def NotSettingProfile(request):
#     profile_emojis = [
#         {"url": "media/profile_images/1.png"},
#         {"url": "media/profile_images/2.png"},
#         {"url": "media/profile_images/3.png"},
#         {"url": "media/profile_images/4.png"},
#         {"url": "media/profile_images/5.png"},
#         {"url": "media/profile_images/6.png"},
#         {"url": "media/profile_images/7.png"},
#         {"url": "media/profile_images/8.png"},
#         {"url": "media/profile_images/9.png"},
#         {"url": "media/profile_images/10.png"},
#         {"url": "media/profile_images/11.png"},
#         {"url": "media/profile_images/12.png"},
#         {"url": "media/profile_images/13.png"},
#         {"url": "media/profile_images/14.png"},
#         {"url": "media/profile_images/15.png"},
#         {"url": "media/profile_images/16.png"},
#         {"url": "media/profile_images/17.png"},
#         {"url": "media/profile_images/18.png"},
#         {"url": "media/profile_images/19.png"},
#         {"url": "media/profile_images/20.png"},
#         {"url": "media/profile_images/21.png"},
#         {"url": "media/profile_images/22.png"},
#         {"url": "media/profile_images/23.png"},
#         {"url": "media/profile_images/24.png"},
#         {"url": "media/profile_images/25.png"},
#         {"url": "media/profile_images/26.png"},
#         {"url": "media/profile_images/27.png"},
#         {"url": "media/profile_images/28.png"},
#         {"url": "media/profile_images/29.png"},
#         {"url": "media/profile_images/30.png"},
#         # 나머지 프로필 이모지도 추가
#     ]
#     skills = Skill.objects.all()
#     context = {
#         "profile_emojis": profile_emojis,
#         "skills": skills
#     }
#     return render(request, 'profiles/detail.html', context)



