from django.test import TestCase, Client
from django.urls import reverse

from .models import Account


class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create_user('user1', 'user1@gymgeek.cz', 'U1', is_active=True)
        Account.objects.create_user('user2', 'user2@gymgeek.cz', 'U2', is_active=True)

        self.client = Client()
        self.client.login(username='user1', password='U1')

    def test_accessibility_of_account_pages(self):
        """Uživatel může upravovat jen svoje informace."""
        # Úprava vlastního účtu
        response = self.client.get(reverse('accounts:edit', args=('user1',)))
        self.assertEqual(response.status_code, 200)

        # Úprava cizího účtu
        response = self.client.get(reverse('accounts:edit', args=('user2',)))
        self.assertEqual(response.status_code, 404)

    def test_account_form_processing(self):
        """Správné zpracování aktualizace informací účtu."""
        url = reverse('accounts:edit', args=('user1',))

        # Správná aktualizace
        response = self.client.post(url, {'about': 'Bez popisu.'})
        self.assertEqual(response.status_code, 302)

        # Nic nezměněno
        response = self.client.post(url, {'about': 'Bez popisu.'})
        self.assertEqual(response.status_code, 200)

        # Nesprávná hodnota (about: max_length=500)
        response = self.client.post(url, {'about': '_'*501})
        self.assertEqual(response.status_code, 200)
