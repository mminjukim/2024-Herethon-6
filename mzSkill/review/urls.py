from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('teacher/<int:teacher_id>/', views.show_review, name='show_review'),
    path('write/<str:teacher_username>/', views.write_review, name = 'write_review'),
    path('<str:teacher_username>/', views.teacher_reviews, name = 'teacher_reviews')
]