from django.shortcuts import render, redirect

from accounts.forms import *
from .forms import *
from .models import *
from django.utils import timezone

# 러너 프로필 보기
def show_learner_profile(request, id):
    profile = Learner.objects.get(id=id)
    return render(request, 'show_learner_profile.html', {'profile':profile})

# 러너 프로필 수정하기
def update_learner_profile(request, id):
    profile = Learner.objects.get(id=id)
    if request.method == 'POST':
        form = WriteLearnerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:show_learner_profile', id)
    else:
        form = WriteLearnerProfileForm(instance=profile)
        return render(request, "update_learner_profile.html", {'form':form})

# 러너 성격 스킬 수정하기 
def update_learner_details(request, id): # 수정
    profile = Learner.objects.get(id=id)
    if request.method == 'POST':
        skills = request.POST.getlist('skills[]')
        profile.skills.set(skills)
        personalities = request.POST.getlist('personalities[]')
        profile.personalities.set(personalities)
        return redirect('profiles:show_learner_profile', id) 
    else:
        return render(request, "update_learner_details.html")


# 티쳐 프로필 보기
def show_teacher_profile(request, id):
    profile = Teacher.objects.get(id=id)
    return render(request, 'show_teacher_profile.html', {'profile':profile})

# 티쳐 프로필 수정하기
def update_teacher_profile(request, id):
    profile = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = WriteTeacherProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:show_teacher_profile', id)
    else:
        form = WriteTeacherProfileForm(instance=profile)
        return render(request, "update_teacher_profile.html", {'form':form})
    
# 티쳐 성격 스킬 수정하기
def update_teacher_details(request, id): 
    profile = Teacher.objects.get(id=id)
    if request.method == 'POST':
        skills = request.POST.getlist('skills[]')
        profile.skills.set(skills)
        personalities = request.POST.getlist('personalities[]')
        profile.personalities.set(personalities)
        return redirect('profiles:show_teacher_profile', id) 
    else:
        return render(request, "update_teacher_details.html")

def write_teachingplan(request, id):
    profile = Teacher.objects.get(id=id)
    if request.method == 'POST':
        profile.bio = request.POST['bio']
        profile.teaching_plan = request.POST['teaching_plan']
        profile.is_paid = request.POST['is_paid']
        profile.save()
        return redirect('profiles:show_teacher_profile', id) 
    else:
        return render(request, "write_teachingplan.html")
    
def appeal_teacher(request, id):
    profile = Teacher.objects.get(id=id)
    profile.last_appealed = timezone.localtime()
    profile.save(update_fields=['last_appealed'])
    return render(request, 'show_teacher_profile.html', {'profile':profile})
