from django.shortcuts import render

# Home page
def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/home.html', context={'title': 'Hlavní stránka'})

    return render(request, 'core/login.html')
