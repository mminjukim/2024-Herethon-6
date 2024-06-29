from django.contrib import admin
from .models import LearnerProfile, TeacherProfile, Personality, Category, Skill, TeachingPlan

admin.site.register(LearnerProfile)
admin.site.register(TeacherProfile)
admin.site.register(Personality)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(TeachingPlan)
