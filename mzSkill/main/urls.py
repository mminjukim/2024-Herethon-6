from django.urls import path
from .views import create_or_edit_teaching_plan, main, profile_card_view, edit_profile_view
from chat.views import room
from . import views

app_name = 'main'

urlpatterns = [
    # 메인함수는 티쳐/러너에 따라 적절하게 반환한다.
    path('', main, name='main'),
    path('profile/', profile_card_view, name='profile_card_view'),
    path('teaching_plan/', create_or_edit_teaching_plan, name='teaching_plan'),
    path('profile/edit/', edit_profile_view, name='edit_profile_view'),
    path('chat/', room, name = 'room'),
]
