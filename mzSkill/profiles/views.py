from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View
from .forms import LearnerProfileForm, RoleChoiceForm, SignUpForm, TeacherProfileForm, TeachingPlanForm
from .models import LearnerProfile, TeacherProfile, TeachingPlan

# 역할 선택 뷰
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
    # 그 데이터를 입력함
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        # 회원가입창을 렌더링 함.
        return render(request, 'profiles/signup.html', {'form': form})

    # 그 데이터를 받아옴
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        # 폼 형식이 적절하면
        if form.is_valid():
            # 폼 저장 뒤
            user = form.save()
            # 로그인 시도
            login(request, user)
            role = request.session.get('role')

            if role == '1':
                return redirect('profiles:detail')
            elif role == '2':
                return redirect('profiles:detail')
        
        return render(request, 'profiles/signup.html', {'form': form})

# 아이디 생성 후 프로필 세부사항 설정 뷰 >> 메인으로 넘어감
class DetailView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        role = request.session.get('role')
        if role == '1':
            form = LearnerProfileForm()
        elif role == '2':
            form = TeacherProfileForm()
        else:
            return redirect('profiles:role_choice')
        return render(request, 'profiles/detail.html', {'form': form})

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

            form.save_m2m()  # Many-to-many 필드 저장

            # 적용 후 내가 바로 보여지는곳
            return redirect('main:main')
        # 컨텍스트 데이터가 렌더링 되는 곳
        return render(request, 'profiles/detail.html', {'form': form})


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
    
    if request.method == "POST":
        form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            teacher_profile = form.save(commit=False)
            teacher_profile.user = user
            teacher_profile.save()

            # 스킬 필드를 명시적으로 업데이트한다.
            form.save_m2m()

            return redirect('profiles:teacher_profile', username=user.username)
    else:
        form = TeacherProfileForm(instance=profile)
    
    return render(request, 'profiles/teacher_profile_edit.html', {'form': form})

# 로그아웃 뷰
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('profiles:login')



