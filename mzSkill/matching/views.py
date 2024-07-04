from django.shortcuts import render, redirect

from django.db.models import Count
from django.db.models.functions import Length

from profiles.models import *

def match_teacher_list(request, learner_id):
    learner = Learner.objects.get(id=learner_id)
    wanting_skills = learner.skills.all()

    teachers = Teacher.objects.filter(skills__in=wanting_skills).exclude(id__in=learner.my_teachers.all()).distinct()

    teacher_scores = []
    for teacher in teachers:
        skill_count = teacher.skills.filter(id__in=wanting_skills).count()
        score = skill_count * 10

        personality_count = teacher.personalities.filter(id__in=learner.personalities.all()).count()
        score += personality_count

        teacher_scores.append((teacher, score))

    teacher_scores = sorted(teacher_scores, key=lambda x:x[1], reverse=True)
    got_teachers = [t[0] for t in teacher_scores]
    
    return render(request, 'match_teacher_list.html', {'got_teachers':got_teachers, 'learner':learner}) 


def mzteacher_profile(request, teacher_id):
    learner = Learner.objects.get(user_id=request.user.id)
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'mzteacher_profile.html', {'teacher':teacher, 'profile':learner})


def match_a_teacher(request, teacher_id):
    learner = Learner.objects.get(user_id=request.user.id)
    teacher = Teacher.objects.get(id=teacher_id)
    learner.my_teachers.add(teacher)
    print(learner.my_teachers.all)
    return render(request, 'match_complete.html', {'teacher':teacher})


def mzteacher_list(request, category_id):
    teachers = Teacher.objects.all()
    categories = Category.objects.all()
    if category_id != 0:
        skills_in_catergory = Skill.objects.filter(category_id=category_id)
        print(skills_in_catergory)
        teachers = Teacher.objects.filter(skills__in=skills_in_catergory).distinct()    
    print(teachers)

    context = {
        'teachers':teachers,
        'categories':categories,
        'category_id':category_id,
    }
    return render(request, 'mzteacher_list.html', context)