from django.test import TestCase
from common_tests.base_tests import BaseTestSetup
from scrum_board.models import Task

# Create your tests here.
class ScrumBoardTest(BaseTestSetup):
    def test_get_scrumBoard(self):
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response =self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        
    def test_post_scrumboard(self):
        task_data = dict(self.TEST_TASK_DATA)
        task_data.pop('author', None)
        task_data['author_username'] = self.user.username
        response =self.client.post('/tasks/', data=task_data, format='json')
        self.assertEqual(response.status_code, 201)
        
        # Check correct data typ
        self.assertEqual(response.data['id'], task_data['id'])
        self.assertEqual(response.data['title'], task_data['title'])
        self.assertEqual(response.data['description'], task_data['description'])
        # self.assertEqual(response.data['author'], task_data['author'])
        self.assertEqual(response.data['author_username'], task_data['author_username'])
        self.assertEqual(response.data['created_at'], task_data['created_at'])
        self.assertEqual(response.data['due_date'], task_data['due_date'])
        self.assertEqual(response.data['priority'], task_data['priority'])
        self.assertEqual(response.data['color'], task_data['color'])
        self.assertEqual(response.data['board_column'], task_data['board_column'])
        
        # Check database correct created
        self.assertTrue(Task.objects.filter(title='Test').exists())