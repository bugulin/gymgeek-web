from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Account
from .models import Lesson


class LessonTestCase(TestCase):

    def setUp(self):
        perm = Permission.objects.get(name='Can see hidden lesson')

        self.lesson1 = Lesson.objects.create(index='0', is_visible=True)
        self.lesson2 = Lesson.objects.create(index='1', is_visible=False)

        self.user1 = Account.objects.create_user('user1', is_active=True)
        self.user2 = Account.objects.create_user('user2', is_active=True)
        self.user2.user_permissions.add(perm)

        self.client = Client()

    def test_user_without_perm(self):
        """Normální uživatel smí přistoupit pouze na viditelné lekce."""
        self.client.force_login(self.user1)

        # Obvyklý dotaz na lekci
        response = self.client.get(reverse('lessons:detail', args=(self.lesson1.index,)))
        self.assertEqual(response.status_code, 200)

        # Dotaz na skrytou lekci
        response = self.client.get(reverse('lessons:detail', args=(self.lesson2.index,)))
        self.assertEqual(response.status_code, 404)

    def test_user_with_perm(self):
        """Uživatel s právy může přistoupit i na skrytou lekci."""
        self.client.force_login(self.user2)

        # Obvyklý dotaz na lekci
        response = self.client.get(reverse('lessons:detail', args=(self.lesson1.index,)))
        self.assertEqual(response.status_code, 200)

        # Dotaz na skrytou lekci
        response = self.client.get(reverse('lessons:detail', args=(self.lesson2.index,)))
        self.assertEqual(response.status_code, 200)
