from django.http import HttpResponse
from django.shortcuts import render

# Home page
def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/home.html', context={'title': 'Hlavní stránka'})

    return render(request, 'core/login.html')

# Health page for Openshift
def health(request):
    return HttpResponse('1')
