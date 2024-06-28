from django.urls import path
from django.contrib import admin
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('rolechoice/', RoleChoiceView.as_view(), name='rolechoice'),
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('profile/', ProfileView.as_view(), name = 'profile'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]