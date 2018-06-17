"""python_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from forum import views
from accounts import views as accounts_views

urlpatterns = [
    path(r'', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^categories/(?P<pk>\d+)/$', views.category_threads, name='category_threads'),
    url(r'^categories/(?P<pk>\d+)/new/$', views.new_thread, name='new_thread'),
    url(r'^categories/(?P<pk>\d+)/threads/(?P<thread_pk>\d+)/$', views.thread_posts, name='thread_posts'),
    url(r'^categories/(?P<pk>\d+)/threads/(?P<thread_pk>\d+)/reply/$', views.reply_thread, name='reply_thread'),
    url(r'^admin/', admin.site.urls),

]
