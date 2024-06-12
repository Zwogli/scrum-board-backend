from django.test import TestCase
from common_tests.base_tests import BaseTestSetup

# Create your tests here.
class LoginTest(BaseTestSetup):
    def test_login(self):
        login_data = {
            'username': self.user.username,
            'password': 'test_password'
        }
        response = self.client.post('/login/', data=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
    
class LogoutTest(BaseTestSetup):
    def test_logout(self):
        response =self.client.post('/logout/')
        self.assertEqual(response.status_code, 200)