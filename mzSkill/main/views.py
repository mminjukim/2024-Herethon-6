from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import LearnerProfile, TeacherProfile, TeachingPlan
from profiles.forms import LearnerProfileForm, TeacherProfileForm, TeachingPlanForm

# 현재 로그인한 사람의 프로필을 가져와야함.
@login_required
def main(request):
    # 프로필 변수 초기화
    profile = None
    try:
        # 러너아니면
        profile = LearnerProfile.objects.get(user_id=request.user.id)
    except LearnerProfile.DoesNotExist:
        try:
            # 티쳐로
            profile = TeacherProfile.objects.get(user_id=request.user.id)
        except TeacherProfile.DoesNotExist:
            pass # 수정
    return render(request, 'main/main.html', {'profile': profile})

# 내 프로필 보기

@login_required
def profile_card_view(request):
    profile = None
    try:
        profile = LearnerProfile.objects.get(user=request.user)
    except LearnerProfile.DoesNotExist:
        try:
            profile = TeacherProfile.objects.get(user=request.user)
        except TeacherProfile.DoesNotExist:
            pass

    template_name = 'main/default_profile.html'

    if isinstance(profile, LearnerProfile):
        template_name = 'main/learner_profile.html'
    elif isinstance(profile, TeacherProfile):
        template_name = 'main/teacher_profile.html'

    return render(request, template_name, {'profile': profile})

# 프로필 수정 함수(러너, 티쳐일때 다르게)
@login_required
def edit_profile_view(request):
    profile = None
    is_learner = False
    is_teacher = False
    template_name = ''  # 템플릿 이름을 기본값으로 초기화
    try:
        profile = LearnerProfile.objects.get(user=request.user)
        is_learner = True
    except LearnerProfile.DoesNotExist:
        try:
            profile = TeacherProfile.objects.get(user=request.user)
            is_teacher = True
        except TeacherProfile.DoesNotExist:
            return redirect('profiles:role_choice')  # 프로필이 없으면 역할 선택 페이지

    if request.method == "POST":
        if is_learner:
            profile_form = LearnerProfileForm(request.POST, request.FILES, instance=profile)
        else:
            profile_form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        
        if profile_form.is_valid():
            profile_form.save()
            return redirect('main:profile_card_view')
    else:  # GET 요청
        if is_learner:
            profile_form = LearnerProfileForm(instance=profile)
            template_name = 'main/learner_profile_edit.html'
        else:
            profile_form = TeacherProfileForm(instance=profile)
            template_name = 'main/teacher_profile_edit.html'

    return render(request, template_name, {'profile_form': profile_form})

@login_required
def main_page(request):
    return render(request, 'main/main.html')

@login_required
def create_or_edit_teaching_plan(request):
    try:
        profile = TeacherProfile.objects.get(user=request.user)
    except TeacherProfile.DoesNotExist:
        profile = None

    if profile:
        try:
            teaching_plan = TeachingPlan.objects.get(profile=profile)
        except TeachingPlan.DoesNotExist:
            teaching_plan = None

        if request.method == "POST":
            form = TeachingPlanForm(request.POST, instance=teaching_plan)
            if form.is_valid():
                teaching_plan = form.save(commit=False)
                teaching_plan.profile = profile
                teaching_plan.save()
                return redirect('main:profile_card_view')
        else:
            form = TeachingPlanForm(instance=teaching_plan)

        return render(request, 'main/edit_teaching_plan.html', {'form': form})
    else:
        return redirect('main:profile_card_view')
