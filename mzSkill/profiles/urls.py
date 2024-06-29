# profiles/urls.py

from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('role/', RoleChoiceView.as_view(), name='role_choice'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # 세부사항 설정할 수 있게끔
    path('detail/', DetailView.as_view(), name = 'detail'),
    # 내 프로필 들어가면 username에 맞는 프로필이 views함수에 의해 템플릿이 렌더링 된다.
    path('profile/learner/<str:username>/', learner_profile_view, name='learner_profile'),
    path('profile/teacher/<str:username>/', teacher_profile_view, name='teacher_profile'),
        # 프로필 수정부분 들어가면 티쳐와 러너 각각에 다른 수정필드가 등장
    path('profile/learner/edit/', learner_profile_edit_view, name='learner_profile_edit'),
    path('profile/teacher/edit/', teacher_profile_edit_view, name='teacher_profile_edit'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]



