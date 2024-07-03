from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('', community, name='community'),

    path('create_post/', create_post, name='create_post'),
    path('create_comment/<int:id>/', create_comment, name='create_comment'),

    path('post_detail/<int:id>/', post_detail, name='post_detail'),

]