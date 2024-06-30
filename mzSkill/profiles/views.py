from django.shortcuts import render, redirect

from accounts.forms import *

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

def update_learner_details(request, id): # 수정
    profile = Learner.objects.get(id=id)
    if request.method == 'POST':
        form = LearnerDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:show_learner_profile', id) # id 위치 어디?
    else:
        form = LearnerDetailsForm(instance=profile)
        return render(request, "update_learner_details.html", {'form':form})

