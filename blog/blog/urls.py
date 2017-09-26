from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?i)$', views.post_list, name='home'),
    url(r'^(?i)blog/add/$', views.post_add, name='post_add'),
    url(r'^(?i)(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
]
