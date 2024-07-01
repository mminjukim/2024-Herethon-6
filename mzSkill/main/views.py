from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import LearnerProfile, TeacherProfile, TeachingPlan
from profiles.forms import LearnerProfileForm, TeacherProfileForm, TeachingPlanForm

# 현재 로그인한 사람의 프로필을 가져와야함.
@login_required
def main(request):
    # 초기화
    profile = None
    # 프로필 설정이 되지않은 이용자들은 기본 반환 템플릿이 필요하다.
    # TypeError at /main/join() argument must be str, bytes, or os.PathLike object, not 'NoneType' 
    template_name = 'main/main.html'
    try:
        profile = LearnerProfile.objects.get(user=request.user)
        template_name = 'main/learner_main.html'  # 러너 메인 페이지 템플릿
    except LearnerProfile.DoesNotExist:
        try:
            profile = TeacherProfile.objects.get(user=request.user)
            template_name = 'main/teacher_main.html'  # 티쳐 메인 페이지 템플릿
        except TeacherProfile.DoesNotExist:
            pass

    return render(request, template_name, {'profile': profile})


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
    teaching_plan_form = None

    try:
        profile = LearnerProfile.objects.get(user=request.user)
        is_learner = True
    except LearnerProfile.DoesNotExist:
        # 티쳐 프로필은 러너와 구분되야함
        try:
            profile = TeacherProfile.objects.get(user=request.user)
            is_teacher = True
            try:
                # 티칭 계획 폼을 적용해야했음.
                teaching_plan = TeachingPlan.objects.get(profile=profile)
            except TeachingPlan.DoesNotExist:
                teaching_plan = None

            if request.method == "POST":
                teaching_plan_form = TeachingPlanForm(request.POST, instance=teaching_plan)
            else:
                teaching_plan_form = TeachingPlanForm(instance=teaching_plan)
        except TeacherProfile.DoesNotExist:
            return redirect('profiles:role_choice')  # 어떤 프로필이 없으면 역할 선택 페이지

    if request.method == "POST":
        if is_learner:
            profile_form = LearnerProfileForm(request.POST, request.FILES, instance=profile)
        else:
            profile_form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        
        if profile_form.is_valid() and (not is_teacher or teaching_plan_form.is_valid()):
            profile_form.save()
            if is_teacher:
                teaching_plan = teaching_plan_form.save(commit=False)
                teaching_plan.profile = profile
                teaching_plan.save()
            return redirect('main:profile_card_view')
    else:  # GET 요청
        if is_learner:
            profile_form = LearnerProfileForm(instance=profile)
            template_name = 'profiles/learner_profile_edit.html'
        else:
            profile_form = TeacherProfileForm(instance=profile)
            template_name = 'profiles/teacher_profile_edit.html'

    return render(request, template_name, {'profile_form': profile_form, 'teaching_plan_form': teaching_plan_form})


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
