from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import new_blog_views


urlpatterns = [

    url(r'^post$',new_blog_views.blog_post, name='blog_post'),
    url(r'^view/(?P<blog_id>[0-9]+)/$', new_blog_views.blog_view, name='blog_view'),
    url(r'^edit/(?P<blog_id>[0-9]+)/$', new_blog_views.edit_post, name='blog_edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
