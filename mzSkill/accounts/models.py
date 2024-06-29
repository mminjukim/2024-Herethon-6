from django.contrib.auth.models import User
from django.db import models

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
    category = models.ForeignKey(Category, related_name = 'skill', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.category_name} - {self.skill_name}"

# 유저 프로필 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    profile_emoji = models.ImageField(blank=True) # upload_to = 디렉터리 경로 작성요망
    birthDate = models.DateField( null = False, blank = False)
    skills = models.ManyToManyField(Skill, related_name='user_profiles')

    ROLE_CHOICES = ((1, '러너'), (2, '티쳐'))
    role = models.PositiveIntegerField(choices=ROLE_CHOICES, null=True) # 러너, 티쳐 role 선택 
    # 참고: https://medium.com/djangotube/django-roles-groups-and-permissions-introduction-a54d1070544

    def __str__(self):
        return self.nickname
    
class TeachingPlan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='teaching_plans')
    expression = models.TextField()
    plan = models.TextField()
    method = models.CharField(max_length=20, choices=[('free', '무료 티칭'), ('paid', '유료 티칭')])
