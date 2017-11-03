from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('index', 'title', 'is_visible')
    search_fields = ('index', 'title')
    ordering = ('index',)
    fieldsets = (
        (None, {'fields': ('index', 'title', 'text', 'date', 'is_visible')}),
    )
