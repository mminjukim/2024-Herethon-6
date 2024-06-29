from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, TeachingPlan, Skill
# UserCreationForm: 기본 유저 생성 폼(pw1 pw2를 제공)

# 티쳐/러너 역할 선택 
class RoleChoiceForm(forms.Form): # 역할 선택 폼
    choice = forms.ChoiceField(
        choices = Profile.ROLE_CHOICES,
        widget=forms.RadioSelect
    )

# 회원가입
class SignUpForm(UserCreationForm):

    class Meta():
        # AUTH_USER_MODEL이라고 settings.py에 정의한 user모델을 가져온다는 의미
        model = User
        fields = ['first_name', 'username', 'email']


# 프로필 등록 
class ProfileForm(forms.ModelForm):
    # 달력형식으로
    birthDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta():
        model = Profile
        fields = ['nickname', 'birthDate', 'profile_emoji']


# 프로필 세부사항 설정
class DetailForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(
        queryset = Skill.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
    )
    
    class Meta:
        model = Profile
        fields = ['skills']

        

#티칭 계획 폼 추가
class TeachingPlanForm(forms.ModelForm):
    class Meta:
        model = TeachingPlan
        fields = ['expression', 'plan', 'method']