from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('', community, name='community'),
]