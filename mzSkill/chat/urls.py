from django.urls import path
from . import views
from .views import *

app_name = 'chat'

urlpatterns = [
    path('', views.room, name='room'),
    path('<str:username>/', views.chat_view, name='chat_view'),
    path('out/<str:username>/', views.out, name='out'),
]