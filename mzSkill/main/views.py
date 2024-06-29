from django.shortcuts import render, redirect
# account에서 로그인 되어 있다는 전제하에
from django.contrib.auth.decorators import login_required
from accounts.views import login
from profiles.models import Learner, Teacher

@login_required
def main(request):
    profile = Learner.objects.get(user_id = request.user.id)
    if profile is None:
        profile = Teacher.objects.get(user_id = request.user.id)
        return render(request, 'teacher_main.html', {'profile':profile})
    else:
        return render(request, 'learner_main.html', {'profile':profile})