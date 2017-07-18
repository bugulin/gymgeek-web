from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Account


class CoreTestCase(TestCase):
    def setUp(self):
        Account.objects.create_user('user', 'user@gymgeek.cz', 'password')
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

    def test_health_page(self):
        """Na adrese '/health' je veřejně přístupná stránka."""
        # Anonymní uživatel
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

        # Registrovaný uživatel
        self.client.login(username='user', password='password')
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
