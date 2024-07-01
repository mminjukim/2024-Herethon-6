from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
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
=======

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

    def __str__(self):
        return self.nickname
>>>>>>> cfabd5778b58d5bb7907903a32c316cee0386ee3
