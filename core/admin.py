from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible', 'is_pinned')
    search_fields = ('title', 'is_pinned')
    ordering = ('-is_visible', '-is_pinned')
    fieldsets = (
        (None, {'fields': ('is_visible', 'is_pinned', 'title', 'text')}),
    )
