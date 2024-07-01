from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('rolechoice/', RoleChoiceView.as_view(), name='rolechoice'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('writeprofile/', WriteProfileView.as_view(), name='writeprofile'),
    path('writedetails/', WriteDetailsView.as_view(), name='writedetails'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]