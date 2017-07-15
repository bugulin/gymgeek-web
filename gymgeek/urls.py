from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    # Django apps
    url(r'^', include('core.urls')),
    url(r'^accounts/', include('accounts.urls')),

    # Authentication
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Admin site
    url(r'^admin/', admin.site.urls),

    # Special static files
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
]
