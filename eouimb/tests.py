from django.contrib.auth.models import User
from django.test import TestCase


class EmailOrUsernameInsensitiveModelBackendTests(TestCase):
    def setUp(self):
        for user, email in [('foo', 'foo@example.org'), ('@nn@', 'anna@example.org')]:
            User.objects.create_user(user, email=email, password=user)

    def test_login(self):
        self.assertTrue(self.client.login(username='foo', password='foo'))
        self.assertTrue(self.client.login(username='fOo', password='foo'))
        self.assertFalse(self.client.login(username='ofo', password='foo'))
        self.assertFalse(self.client.login(username='foo', password='fOo'))
        self.assertTrue(self.client.login(username='foo@example.org', password='foo'))
        self.assertTrue(self.client.login(username='@Nn@', password='@nn@'))
        self.assertTrue(self.client.login(username='ANNA@example.org', password='@nn@'))
