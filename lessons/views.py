from django.shortcuts import render
from .models import Lesson

def index(request):
    return render(request, 'lessons/index.html', context={'title': 'Seznam lekcí', 'lessons': Lesson.objects.filter(is_visible=True).order_by('index', 'date')})
