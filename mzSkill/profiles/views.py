from django.shortcuts import render, redirect

from accounts.forms import *
from .forms import *
from .models import *



# 러너 프로필 보기, 수정 

def show_learner_profile(request, id):
    profile = Learner.objects.get(id=id)
    return render(request, 'show_learner_profile.html', {'profile':profile})

def update_learner_profile(request, id):
    profile = Learner.objects.get(id=id)
    if request.method == 'POST':
        form = WriteLearnerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:update_learner_details', id)
    else:
        form = WriteLearnerProfileForm(instance=profile)
        return render(request, "update_learner_profile.html", {'form':form})

def update_learner_details(request, id):
    profile = Learner.objects.get(id=id)
    if request.method == 'POST':
        form = LearnerDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:show_learner_profile', id) 
    else:
        form = LearnerDetailsForm(instance=profile)
        return render(request, "update_learner_details.html", {'form':form})



# 티쳐 프로필 보기, 수정  

def show_teacher_profile(request, id):
    profile = Teacher.objects.get(id=id)
    return render(request, 'show_teacher_profile.html', {'profile':profile})

def update_teacher_profile(request, id):
    profile = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = WriteTeacherProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:update_teacher_details', id)
    else:
        form = WriteTeacherProfileForm(instance=profile)
        return render(request, "update_teacher_profile.html", {'form':form})

def update_teacher_details(request, id): 
    profile = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:write_teachingplan', id) 
    else:
        form = TeacherDetailsForm(instance=profile)
        return render(request, "update_teacher_details.html", {'form':form})

def write_teachingplan(request, id):
    profile = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeachingPlanForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:show_teacher_profile', id) 
    else:
        form = TeachingPlanForm(instance=profile)
        return render(request, "write_teachingplan.html", {'form':form})