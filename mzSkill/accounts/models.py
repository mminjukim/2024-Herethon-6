from django.db import models
from django.contrib.auth.models import User


# 큰 카테고리
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name


# 세부 스킬 
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.category_name} - {self.skill_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    profile_emoji = models.ImageField(blank=True)
    birthDate = models.DateField(null=False, blank=False)
    skills = models.ManyToManyField(Skill, related_name='user_profiles')

    def __str__(self):
        return self.nickname
