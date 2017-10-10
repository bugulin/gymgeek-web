from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from markdown import markdown

register = template.Library()

@register.filter(name='markdown')
@stringfilter
def markdown_to_html5(text):
    return mark_safe(markdown(conditional_escape(text), output_format='html5', extensions=['markdown.extensions.fenced_code']).replace('<a ', '<a target=\'_blank\''))
