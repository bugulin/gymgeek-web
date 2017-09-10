from social_core.pipeline.partial import partial

@partial
def authorize(strategy, is_new, **kwargs):
    if is_new:
        auth_key = strategy.session_get('auth_key', False)
        strategy.session_set('auth_key', False)

        if auth_key == 'the secret key':
            pass
        else:
            return strategy.redirect('accounts:authorization')

# Saving google data
def set_extra_data(backend, strategy, details, response, user, *args, **kwargs):
    updated = False

    if backend.name == 'google-oauth2':
        image_url = response['image'].get('url')
        google_url = response.get('url')

        if image_url not in (None, user.avatar):
            user.avatar = image_url
            updated = True

        if google_url not in (None, user.url):
            user.url = google_url
            updated = True

    if updated:
        user.save()
