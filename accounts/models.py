from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Account(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'))

    avatar = models.CharField(_('profile image'), max_length=150)
    url = models.CharField(_('google+ page'), max_length=50)
    about = models.TextField(_('description'), max_length=500, blank=True)
