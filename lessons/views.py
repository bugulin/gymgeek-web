from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Lesson

# All lessons
def index(request):
    lessons = Lesson.objects.all() if request.user.has_perm('lessons.see_hidden_lesson') else Lesson.objects.filter(is_visible=True)
    return render(request, 'lessons/index.html', context={'title': 'Seznam lekcí', 'lessons': lessons.order_by('index', 'date')})

# Lesson detail
def detail(request, index):
    lesson = get_object_or_404(Lesson, index=index)

    if lesson.is_visible or request.user.has_perm('lessons.see_hidden_lesson'):
        text = lesson.text.read() if lesson.text else 'Chyba: žádný soubor.'
        return render(request, 'lessons/detail.html', context={'title': 'Lekce č. {}'.format(lesson.index), 'parent_page': reverse('lessons:index'), 'lesson': lesson, 'text': text})
    else:
        raise Http404
