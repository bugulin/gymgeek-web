from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('title'), max_length=50)
    text = models.TextField(_('text'), max_length=2000)

    is_visible = models.BooleanField(_('visible'), default=True)
    is_pinned = models.BooleanField(_('pinned'), default=False)

    def __str__(self):
        return self.title
