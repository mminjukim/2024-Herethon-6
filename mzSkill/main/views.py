from django.shortcuts import render, redirect
# account에서 로그인 되어 있다는 전제하에
from django.contrib.auth.decorators import login_required
from accounts.views import login
from profiles.models import Learner, Teacher
from django.core.paginator import Paginator

@login_required
def main(request):
    teachers = Teacher.objects.all().order_by('-last_appealed')
    teacher_pg = Paginator(teachers, 3)
    pgnum = request.GET.get('page')
    teachers = teacher_pg.get_page(pgnum)

    profile = None
    try:
        profile = Learner.objects.get(user_id = request.user.id)
        return render(request, 'learner_main.html', {'profile':profile, 'teachers':teachers})
    except Learner.DoesNotExist:
        try:
            profile = Teacher.objects.get(user_id = request.user.id)
            return render(request, 'teacher_main.html', {'profile':profile, 'teachers':teachers})
        except Teacher.DoesNotExist:
            pass