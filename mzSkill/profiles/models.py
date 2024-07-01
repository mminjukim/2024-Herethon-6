from django.db import models
from django.contrib.auth.models import User


# 러너/티쳐 성격 타입
class Personality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# 큰 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# 세부 스킬 
class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name = 'skill', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} > {self.name}"


# 러너 프로필 
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=40, blank=True)
    emoji = models.ImageField(blank=True) # upload_to = 디렉터리 경로 작성요망
    birthdate = models.DateField(null = True, blank = False)

    skills = models.ManyToManyField(Skill, related_name='learner_wanting')
    personalities = models.ManyToManyField(Personality, related_name='learner_wanting')

    def __str__(self):
        return self.nickname
    

# 티쳐 프로필 
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=40, blank=True)
    emoji = models.ImageField(blank=True) # upload_to = 디렉터리 경로 작성요망
    birthdate = models.DateField(null = True, blank = False)

    skills = models.ManyToManyField(Skill, related_name='teacher_giving')
    personalities = models.ManyToManyField(Personality, related_name='teacher_giving')

    bio = models.CharField(max_length=300, null=True)
    teaching_plan = models.TextField(null=True)
    is_paid = models.BooleanField(null=True)

    def __str__(self):
        return self.nickname