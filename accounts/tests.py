from django.test import TestCase, Client
from django.urls import reverse

from .models import Account


class AccountTestCase(TestCase):

    def setUp(self):
        self.user1 = Account.objects.create_user('user1', is_active=True)
        self.user2 = Account.objects.create_user('user2', is_active=True)

        self.client = Client()
        self.client.force_login(self.user1)

    def test_accessibility_of_account_pages(self):
        """Uživatel smí upravovat pouze svoje informace."""

        # Úprava vlastního účtu
        response = self.client.get(reverse('accounts:edit', args=(self.user1.username,)))
        self.assertEqual(response.status_code, 200)

        # Úprava cizího účtu
        response = self.client.get(reverse('accounts:edit', args=(self.user2.username,)))
        self.assertEqual(response.status_code, 404)

    def test_account_form_processing(self):
        """Správné zpracování aktualizace informací účtu."""
        url = reverse('accounts:edit', args=(self.user1.username,))

        # Správná aktualizace
        response = self.client.post(url, {'about': 'Bez popisu.'})
        self.assertEqual(response.status_code, 302)

        # Nic nezměněno
        response = self.client.post(url, {'about': 'Bez popisu.'})
        self.assertEqual(response.status_code, 200)

        # Nesprávná hodnota (about: max_length=500)
        response = self.client.post(url, {'about': '_'*501})
        self.assertEqual(response.status_code, 200)
