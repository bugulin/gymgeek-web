from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date
from core.storage import OverwriteStorage

def lesson_content_path(instance, filename):
    return 'lessons/{}.rst'.format(instance.index)


class Lesson(models.Model):
    index = models.IntegerField(_('index'), unique=True)
    title = models.CharField(_('title'), max_length=75)
    date = models.DateField(_('date'), default=date.today)
    text = models.FileField(_('content of the lesson'), storage=OverwriteStorage(), upload_to=lesson_content_path)

    is_visible = models.BooleanField(_('visible'), default=False)

    def __str__(self):
        return '{}. {}'.format(self.index, self.title)
