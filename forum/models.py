from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=256)
    description = models.CharField(max_length=100)


class Forum_Thread(models.Model):
    thread_name = models.CharField(max_length=256)
    update_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)

    def __str__(self):
        return self.thread_name


class Post(models.Model):
    content = models.CharField(max_length=512)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    forum_thread = models.ForeignKey(Forum_Thread, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
