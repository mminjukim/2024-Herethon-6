from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profiles.models import *


# 티쳐/러너 역할 선택 
class RoleChoiceForm(forms.Form): # 역할 선택 폼
    usertype = forms.ChoiceField(
        label='사용자 유형',
        choices=((1, '러너'), (2, '티쳐')),
        widget=forms.RadioSelect
    )


# 회원가입 
class SignUpForm(UserCreationForm):

    class Meta():
        # AUTH_USER_MODEL이라고 settings.py에 정의한 user모델을 가져온다는 의미
        model = User
        fields = ['first_name', 'username', 'email']


# 러너/티쳐 프로필 설정 
class WriteLearnerProfileForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta():
        model = Learner
        fields = ['nickname', 'birthdate', 'emoji']

class WriteTeacherProfileForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta():
        model = Teacher
        fields = ['nickname', 'birthdate', 'emoji']


# 러너/티쳐 세부 프로필 설정 
class LearnerDetailsForm(forms.ModelForm):

    personalities = forms.ModelMultipleChoiceField(
        queryset = Personality.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
    )
    skills = forms.ModelMultipleChoiceField(
        queryset = Skill.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
    )
    
    class Meta:
        model = Learner
        fields = ['skills', 'personalities']

class TeacherDetailsForm(forms.ModelForm):

    personalities = forms.ModelMultipleChoiceField(
        queryset = Personality.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
    )
    skills = forms.ModelMultipleChoiceField(
        queryset = Skill.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
    )
    
    class Meta:
        model = Learner
        fields = ['skills', 'personalities']