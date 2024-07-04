from django.urls import path
from .views import *

app_name = 'matching'

urlpatterns = [
    path('<int:learner_id>/', match_teacher_list, name='match_teacher_list'),
    path('mzteacher_profile/<int:teacher_id>/', mzteacher_profile, name='mzteacher_profile'),
    path('mzteacher_profile/<int:teacher_id>/match/', match_a_teacher, name='match_a_teacher'),

    path('mzteachers/', mzteacher_list, name='mzteacher_list'),
]