from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import ugettext_lazy as _

class AuthKey(models.Model):
    code = models.CharField(_('secret code'), max_length=32, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Account(AbstractUser):
    is_active = models.BooleanField(_('active'), default=False)

    avatar = models.CharField(_('profile image'), max_length=250, blank=True)
    url = models.CharField(_('google+ page'), max_length=75, blank=True)
    about = models.TextField(_('description'), max_length=500, blank=True)
