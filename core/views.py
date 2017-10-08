from django.http import HttpResponse
from django.shortcuts import render

from .models import  Post

# Home page
def home(request):
    if request.user.is_authenticated():
        posts = Post.objects.filter(is_visible=True).order_by('-is_pinned')
        return render(request, 'core/home.html', context={'title': 'Hlavní stránka', 'posts': posts})

    return render(request, 'core/login.html')
