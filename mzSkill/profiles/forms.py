from django import forms
from .models import LearnerProfile, Skill, TeacherProfile, TeachingPlan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoleChoiceForm(forms.Form):
    ROLE_CHOICES = [
        (1, '러너'),
        (2, '티쳐'),
    ]
    choice = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

# 회원가입
class SignUpForm(UserCreationForm):

    class Meta():
        # AUTH_USER_MODEL이라고 settings.py에 정의한 user모델을 가져온다는 의미
        model = User
        fields = ['first_name', 'username', 'email']

class LearnerProfileForm(forms.ModelForm):
    birthDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    skills = forms.ModelMultipleChoiceField(
    queryset=Skill.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True
    )
    
    class Meta:
        model = LearnerProfile
        fields = ['nickname', 'birthDate', 'profile_emoji', 'skills']

class TeacherProfileForm(forms.ModelForm):
    birthDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    skills = forms.ModelMultipleChoiceField(
    queryset=Skill.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True
    )
    
    class Meta:
        model = TeacherProfile
        fields = ['nickname', 'birthDate', 'profile_emoji', 'skills']

# 프로필 세부사항 설정(스킬 선택)
class DetailForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(
        queryset = Skill.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
    )
    
    class Meta:
        fields = ['skills']

#티칭 계획 폼 추가
class TeachingPlanForm(forms.ModelForm):
    class Meta:
        model = TeachingPlan
        fields = ['expression', 'plan', 'method']