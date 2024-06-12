from django.test import TestCase
from common_tests.base_tests import BaseTestSetup

# Create your tests here.
class ScrumBoardTest(BaseTestSetup):
    def test_scrumboardpage(self):
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response =self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)