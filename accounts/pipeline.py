from social_core.pipeline.partial import partial
from .models import AuthKey

@partial
def authorize(strategy, user, **kwargs):
    if user.is_active:
        return

    auth_key = strategy.session_get('auth_key', False)
    if auth_key: del strategy.session['auth_key']

    if auth_key:
        authorized = False
        for key in AuthKey.objects.all():
            if auth_key == key.code:
                user.groups.add(key.group)
                user.is_active = True
                if user.has_perm('accounts.staff_access'): user.is_staff = True
                user.save()
                break
        return

    return strategy.redirect('accounts:authorization')

# Saving google data
def load_extra_data(backend, strategy, details, response, user, *args, **kwargs):
    if backend.name == 'google-oauth2':
        user.avatar = response['image'].get('url')
        user.url = response.get('url')
