from django.contrib import admin
from .models import Category, Forum_Thread, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Forum_Thread)
admin.site.register(Post)