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
        my_teachers = profile.my_teachers.all()
        teacher_pg = Paginator(my_teachers, 3)
        my_teachers = teacher_pg.get_page(pgnum)
        return render(request, 'learner_main.html', {'profile':profile, 'teachers':teachers, 'my_teachers':my_teachers})
    except Learner.DoesNotExist:
        try:
            profile = Teacher.objects.get(user_id = request.user.id)
            my_learners = profile.my_learners.all()
            learner_pg = Paginator(my_learners, 3)
            my_learners = learner_pg.get_page(pgnum)
            return render(request, 'teacher_main.html', {'profile':profile, 'teachers':teachers, 'my_learners':my_learners})
        except Teacher.DoesNotExist:
            pass