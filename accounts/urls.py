from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>[\w\.]+)/$', views.detail, name='detail'),
    url(r'^(?P<username>[\w\.]+)/edit/$', views.edit, name='edit'),
]
