from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Account


class CoreTestCase(TestCase):
    def setUp(self):
        Account.is_active = True
        Account.objects.create_user('user', 'user@gymgeek.cz', 'password', is_active=True)
        self.client = Client()

    def test_home_page(self):
        """Přihlášený uživatel vidí na adrese '/' domovskou stránku (home.html), zatímco nepřihlášený obrazovku s přihlašovacím odkazem (login.html)."""
        # Anonymní uživatel
        response = self.client.get('/')
        self.assertEqual(response.templates[0].name, 'core/login.html')
        self.assertIn('href=\"{}\"'.format(reverse('social:begin', args=('google-oauth2',))), str(response.content))

        # Registrovaný uživatel
        self.client.login(username='user', password='password')
        response = self.client.get('/')
        self.assertEqual(response.templates[0].name, 'core/home.html')

    def test_login_required_middleware(self):
        """Testování 'LoginRequiredMiddleware' ve složce 'decorators.py' pro dostupnosti stránek bez a s přihlášením."""
        # Bez přihlášení
        response = self.client.get(reverse('social:begin', args=('google-oauth2',)))
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/favicon.ico')
        self.assertIn(response.status_code, {200, 301})

        response = self.client.get(reverse('accounts:index'))
        self.assertEqual(response.status_code, 404)

        # S přihlášením
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('social:begin', args=('google-oauth2',)))
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/favicon.ico')
        self.assertIn(response.status_code, {200, 301})

        response = self.client.get(reverse('accounts:index'))
        self.assertEqual(response.status_code, 200)
