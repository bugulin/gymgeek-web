from django.shortcuts import get_object_or_404, render
from .models import Account

# All accounts
def index(request):
    return render(request, 'accounts/index.html', context={'title': 'Uživatelé', 'accounts': Account.objects.all()})

def detail(request, username):
    account = get_object_or_404(Account, username=username)
    return render(request, 'accounts/detail.html', context={'title': 'Uživatel %s' % account.username, 'account': account})
