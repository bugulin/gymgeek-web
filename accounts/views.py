from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Account
from .forms import AboutForm

def can_edit_account(user, account):
    return user.has_perm('accounts.edit') or user == account


# All accounts
def index(request):
    return render(request, 'accounts/index.html', context={'title': 'Uživatelé', 'accounts': Account.objects.all()})

# Account detail
def detail(request, username):
    account = get_object_or_404(Account, username=username)
    return render(request, 'accounts/detail.html', context={'title': 'Uživatel %s' % account.username, 'account': account, 'can_edit': can_edit_account(request.user, account)})

# Account editing
def edit(request, username):
    account = get_object_or_404(Account, username=username)

    if can_edit_account(request.user, account):
        form = AboutForm(request.POST)
        # Dodělat zpracování formuláře
        return render(request, 'accounts/edit.html', context={'title': 'Upravit informace', 'parent_page': reverse('accounts:detail', args=(account.username,)), 'account': account, 'form': form})
    else:
        raise Http404
