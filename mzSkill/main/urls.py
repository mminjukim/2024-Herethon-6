from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('chat/', include('chat.urls')),  # chat 앱 URL 포함
]
