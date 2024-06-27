from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# UserCreationForm: 기본 유저 생성 폼(pw1 pw2를 제공)

class SignUpForm(UserCreationForm):

    class Meta():
        # AUTH_USER_MODEL이라고 settings.py에 정의한 user모델을 가져온다는 의미
        model = User
        fields = ['first_name', 'username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'birthdate', 'profile_emoji']