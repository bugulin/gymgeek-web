from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Account
from .forms import AboutForm

def can_edit_account(user, account):
    return user.has_perm('accounts.edit') or user == account

# Authorization of new account
def authorization(request):
    if request.method == 'POST':
        request.session['auth_key'] = request.POST.get('auth_key')
        return redirect('social:complete', backend='google-oauth2')

    return render(request, 'accounts/authorization.html', context={'title': 'Autorizace'})

# All accounts
def index(request):
    return render(request, 'accounts/index.html', context={'title': 'Uživatelé', 'accounts': Account.objects.order_by('last_name', 'first_name')})

# Account detail
def detail(request, username):
    account = get_object_or_404(Account, username=username)
    return render(request, 'accounts/detail.html', context={'title': 'Uživatel %s' % account.username, 'account': account, 'can_edit': can_edit_account(request.user, account)})

# Account editing
def edit(request, username):
    account = get_object_or_404(Account, username=username)

    if can_edit_account(request.user, account):
        if request.method == 'POST':
            form = AboutForm(request.POST)

            if form.is_valid():
                updated = False

                new_about = form.cleaned_data['about']
                if new_about != account.about:
                    updated = True

                if updated:
                    account.about = new_about
                    account.save()

                    messages.success(request, 'Účet aktualizován.')
                    return HttpResponseRedirect(reverse('accounts:detail', args=(account.username,)))
                else:
                    messages.error(request, 'Nic k aktualizaci.')
        else:
            form = AboutForm(initial={'about': account.about})

        return render(request, 'accounts/edit.html', context={'title': 'Upravit informace', 'parent_page': reverse('accounts:detail', args=(account.username,)), 'account': account, 'form': form})
    else:
        raise Http404
