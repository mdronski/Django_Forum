from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import Truncator


class Category(models.Model):
    category_name = models.CharField(max_length=256)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    def get_thread_count(self):
        return Post.objects.filter(forum_thread__category=self).count()

    def get_last_post(self):
        return Post.objects.filter(forum_thread__category=self).order_by('-creation_date').first()


class Forum_Thread(models.Model):
    thread_name = models.CharField(max_length=256)
    update_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.thread_name


class Post(models.Model):
    content = models.CharField(max_length=512)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    forum_thread = models.ForeignKey(Forum_Thread, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        trun_content = Truncator(self.content)
        return trun_content.chars(32)
