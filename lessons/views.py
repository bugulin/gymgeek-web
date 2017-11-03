from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Lesson

# All lessons
def index(request):
    return render(request, 'lessons/index.html', context={'title': 'Seznam lekcí', 'lessons': Lesson.objects.filter(is_visible=True).order_by('index', 'date')})

# Lesson detail
def detail(request, index):
    lesson = get_object_or_404(Lesson, index=index)
    text = lesson.text.read()
    return render(request, 'lessons/detail.html', context={'title': 'Lekce č. {}'.format(lesson.index), 'parent_page': reverse('lessons:index'), 'lesson': lesson, 'text': text})
