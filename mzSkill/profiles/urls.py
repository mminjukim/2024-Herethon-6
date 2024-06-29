from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('learner/<int:id>/', show_learner_profile, name='show_learner_profile'),
    path('learner/<int:id>/updateprofile/', update_learner_profile, name='update_learner_profile'),
    path('learner/<int:id>/updatedetails/', update_learner_details, name='update_learner_details'),

]