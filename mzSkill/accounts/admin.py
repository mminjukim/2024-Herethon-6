from django.contrib import admin
from .models import Profile, Category, Skill

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Profile)


# Register your models here.
