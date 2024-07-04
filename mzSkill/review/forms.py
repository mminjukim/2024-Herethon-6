from django import forms
from .models import Review

# 리뷰작성폼 정의
# 참고: https://stackoverflow.com/questions/37024650/specify-max-and-min-in-numberinput-widget
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': '티칭 만족도',
            'comment': '티칭에 대한 리뷰',
        }
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'placeholder': '리뷰를 작성해주세요.', 'rows': 5, 'cols': 40}),
        }