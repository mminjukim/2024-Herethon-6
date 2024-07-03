from django.db import models
from django.contrib.auth.models import User
from profiles.models import Learner, Teacher, Category

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='my_post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')

    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):  
        return self.title
    

class Comment(models.Model):
    linked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    content = models.CharField(max_length=300, verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='my_comment')    

    def __str__(self):  
        return self.content