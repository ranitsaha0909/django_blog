from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.user_management_views.post_user_login, name='post_user_list'),
    url(r'^signup$', views.user_management_views.post_new_user, name='post_new_user'),
    url(r'^blog_list$', views.user_management_views.post_user_login, name='post_user_list'),
    url(r'^login$', views.user_management_views.post_user_login, name='post_user_login'),
    url(r'^logout/$', views.user_management_views.user_logout, name='user_logout'),

]
