from django import forms
from django.contrib.auth.models import User
from .models import Teacher

class TeachingPlanForm(forms.ModelForm):
    is_paid = forms.ChoiceField(
        label='티칭 방법',
        choices=((False, '무료 티칭'), (True, '유료 티칭')),
        widget=forms.RadioSelect
    )

    class Meta:
        model = Teacher
        fields = ['bio', 'teaching_plan', 'is_paid']