from django.db import models
from django.contrib.auth.models import AbstractUser, Group as DjangoGroup
from django.utils.translation import ugettext_lazy as _

class Group(DjangoGroup):
    code = models.CharField(_('secret code'), max_length=32)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class Account(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'))

    avatar = models.CharField(_('profile image'), max_length=250)
    url = models.CharField(_('google+ page'), max_length=75)
    about = models.TextField(_('description'), max_length=500, blank=True)

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name="account_set", related_query_name="account")
