"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from user_management.urls import *
from user_management.views.user_management_views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^user/', include('user_management.urls')),
    url(r'^blog/', include('new_blog.urls')),
    #url(r'user_created.html', include('user_management/templates/user_created.html')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
