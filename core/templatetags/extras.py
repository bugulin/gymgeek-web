from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from docutils.core import publish_parts

register = template.Library()

@register.filter(name='rst')
@stringfilter
def rst_to_html5(text):
    parts = publish_parts(text, writer_name='html5', settings_overrides={'initial_header_level': 2})
    return mark_safe(parts['html_title'] + parts['body'])
