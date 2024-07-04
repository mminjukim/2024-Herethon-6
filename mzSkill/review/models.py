from django.db import models
from django.contrib.auth.models import User
from profiles.models import Teacher

class Review(models.Model):
    #CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제
    teacher = models.ForeignKey(Teacher, related_name ='reviews', on_delete = models.CASCADE)
    learner = models.ForeignKey(User, related_name ='reviews', on_delete = models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.learner.username} review of {self.teacher.user.username}'