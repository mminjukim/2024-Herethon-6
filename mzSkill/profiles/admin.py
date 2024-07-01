from django.contrib import admin
<<<<<<< HEAD
from .models import LearnerProfile, TeacherProfile, Personality, Category, Skill, TeachingPlan

admin.site.register(LearnerProfile)
admin.site.register(TeacherProfile)
admin.site.register(Personality)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(TeachingPlan)
=======
from .models import *

admin.site.register(Personality)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Learner)
admin.site.register(Teacher)
>>>>>>> cfabd5778b58d5bb7907903a32c316cee0386ee3
