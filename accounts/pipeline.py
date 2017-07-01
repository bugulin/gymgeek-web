def get_extra_data(backend, strategy, details, response, user, *args, **kwargs):
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
