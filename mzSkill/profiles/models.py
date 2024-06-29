from django.db import models
from django.contrib.auth.models import User

# 러너/티쳐 성격 타입
class Personality(models.Model):
    personality_name = models.CharField(max_length=50)

    def __str__(self):
        return self.personality_name

# 큰 카테고리
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

# 세부 스킬
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.category_name} - {self.skill_name}"

# 러너 프로필 
class LearnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    profile_emoji = models.ImageField(blank=True)
    birthDate = models.DateField(null=False, blank=False)
    skills = models.ManyToManyField(Skill, related_name='learner_profiles')

    def __str__(self):
        return self.nickname

# 티쳐 프로필 
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    profile_emoji = models.ImageField(blank=True) 
    birthDate = models.DateField( null = False, blank = False)
    skills = models.ManyToManyField(Skill, related_name='teacher_profiles')

    def __str__(self):
        return self.nickname
   
# 티칭계획작성
class TeachingPlan(models.Model):
    profile = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='teaching_plans')
    expression = models.TextField()
    plan = models.TextField()
    method = models.CharField(max_length=20, choices=[('free', '무료 티칭'), ('paid', '유료 티칭')])