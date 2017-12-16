from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date
from core.storage import storage

def lesson_content_path(instance, filename):
    return 'lessons/{:02d}.txt'.format(instance.index)


class Lesson(models.Model):
    index = models.IntegerField(_('index'), unique=True)
    title = models.CharField(_('title'), max_length=75)
    date = models.DateField(_('date'), default=date.today)
    text = models.FileField(_('content of the lesson'), storage=storage, upload_to=lesson_content_path)

    is_visible = models.BooleanField(_('visible'), default=False)

    class Meta:
        permissions = (
            ('see_hidden_lesson', 'Can see hidden lesson'),
        )

    def __str__(self):
        return '{}. {}'.format(self.index, self.title)
