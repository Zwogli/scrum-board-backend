from django.test import TestCase
from common_tests.base_tests import BaseTestSetup

# Create your tests here.
class LogoutTest(BaseTestSetup):
    def test_logout(self):
        response =self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)