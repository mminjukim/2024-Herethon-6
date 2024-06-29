from django.urls import path
from .views import create_or_edit_teaching_plan, main, edit_ProfileView, profile_card_view
from chat.views import room

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('Profile/', profile_card_view, name = 'profile_card_view'),
    path('edit_Profile/', edit_ProfileView, name='edit_profile'),
    path('teaching_plan/', create_or_edit_teaching_plan, name='teaching_plan'),
    path('chat/', room, name = 'room'),
]
