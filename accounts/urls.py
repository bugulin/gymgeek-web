from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>.+)/$', views.detail, name='detail')
]
