from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from re import compile


# Uživatel nemusí být přihlášen
URLS_1 =  (
    r'^$',
    r'^health$',

    r'^favicon.ico$',
    r'^{}$'.format(static('images/favicon.ico').lstrip('/')),
    r'^{}$'.format(static('images/wallpaper.png').lstrip('/')),
    r'^{}$'.format(static('images/gymgeek-academy.png').lstrip('/')),
)

# Uživatel nesmí být přihlášen
URLS_2 = (
    r'^oauth/',
)

URLS1 = [compile(expr) for expr in (URLS_1 + URLS_2)]
URLS2 = [compile(expr) for expr in URLS_2]


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path_info.lstrip('/')

        if request.user.is_authenticated():
            if any(url.match(path) for url in URLS2):
                raise Http404
        else:
            if not any(url.match(path) for url in URLS1):
                raise Http404
