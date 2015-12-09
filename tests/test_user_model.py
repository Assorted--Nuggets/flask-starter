import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(first_name='test', last_name='user', username='testuser', password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(first_name='test', last_name='user', username='testuser', password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(first_name='test', last_name='user', username='testuser', password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_random(self):
        u = User(first_name='test', last_name='user', username='testuser', password='cat')
        u2 = User(first_name='test2', last_name='user2', username='testuser2', password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)

