from django.shortcuts import render, redirect
# account에서 로그인 되어 있다는 전제하에
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileForm, TeachingPlanForm
from accounts.models import Profile, TeachingPlan

@login_required
def main(request):
    return render(request, 'main/main.html')

# 사용자 프로필란
@login_required
def profile_card_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    template_name = 'main/default_profile.html'  # 기본 템플릿 설정

    if profile:
        if profile.role == 1: # 러너
            template_name = 'main/runner.html'
        elif profile.role == 2: # 티쳐
            template_name = 'main/teacher.html'
    
    return render(request, template_name, {'profile': profile})

# 프로필 수정 함수
@login_required
def edit_ProfileView(request):
    try:
        # 현재 존재하는 사용자의 프로필을 가져온다.
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == "POST":
        # 프로필 폼 모델 가져오는 변수
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            # 저장 후 메인 페이지로 리디렉션하기
            return redirect('main:profile_card_view')
    else: # GET 요청
        profile_form = ProfileForm(instance=profile)
    
    return render(request, 'main/Edit_profile.html', {'profile_form': profile_form})

@login_required
def main_page(request):
    return render(request, 'main/main.html')


#티칭 계획뷰 추가
@login_required
def create_or_edit_teaching_plan(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
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