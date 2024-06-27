from django.contrib.auth.models import User
from django.db import models


# 큰 카테고리
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name = 'skill', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.category_name} - {self.skill_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    profile_emoji = models.ImageField(blank=True) # upload_to = 디렉터리 경로 작성요망
    birthDate = models.DateField( null = False, blank = False)
    skills = models.ManyToManyField(Skill, related_name='user_profiles')

    def __str__(self):
        return self.nickname
