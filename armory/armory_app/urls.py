from django.conf.urls import urlfrom . import views

app_name = 'armory_app'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),    # ex: /blog/    url(r'^blog/(?P<req>[0-9]+)/$', views.blog, name='blog'),    # ex: /blog/1    url(r'^blog/detail/(?P<req>[0-9]+)/$', views.blog_detail, name='blog_detail'),    # ex: /includes/$    url(r'^includes/(?P<req_file>.+)/$', views.includes, name='includes'),
    # ex: /armory_app/5/comment/
 #   url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
]