from django.test import TestCase

# Create your tests here.
class ScrumBoardTest(TestCase):
    def test_scrumboardpage(self):
        response =self.client.get('/tasks/')
        self.assertEqual(response.satus_code, 200)