from django.conf.urls import url

from . import views

app_name = 'lessons'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
