from django.conf.urls import url

from . import views

app_name = 'lessons'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<index>-?[0-9]+)$', views.detail, name='detail'),
]
