from django.conf.urls import url
armory_appfrom . import views

app_name = 'armory_app'
urlpatterns = [
    # ex: /armory_app/
    url(r'^$', views.index, name='index'),
    # ex: /armory_app/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /armory_app/5/comment/
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
]