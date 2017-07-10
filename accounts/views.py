from django.shortcuts import render
from .models import Account

# All accounts
def index(request):
    return render(request, 'accounts/index.html', context={'title': 'Účty', 'accounts': Account.objects.all()})
