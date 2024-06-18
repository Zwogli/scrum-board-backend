from django.test import TestCase
from common_tests.base_tests import BaseTestSetup
from scrum_board.models import Task
from rest_framework import status

# Create your tests here.
class ScrumBoardTest(BaseTestSetup):
    def test_get_scrumBoard(self):
        response =self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
    
    
    def test_post_scrumboard(self):
        task_data = self.TEST_TASK_DATA.copy()
        task_data['author_username'] = self.user.username
        response =self.client.post('/tasks/', data=task_data, format='json')
        self.assertEqual(response.status_code, 201)
        
        # Check correct data typ
        self.assertEqual(response.data['id'], task_data['id'])
        self.assertEqual(response.data['title'], task_data['title'])
        self.assertEqual(response.data['description'], task_data['description'])
        self.assertEqual(response.data['author_username'], task_data['author_username'])
        self.assertEqual(response.data['created_at'], task_data['created_at'])
        self.assertEqual(response.data['due_date'], task_data['due_date'])
        self.assertEqual(response.data['priority'], task_data['priority'])
        self.assertEqual(response.data['color'], task_data['color'])
        self.assertEqual(response.data['board_column'], task_data['board_column'])
        
        # Check database correct created
        self.assertTrue(Task.objects.filter(title='Test').exists())
        
    
    def test_put_scrumboard(self):
        task = self.create_task()
        self.assertTrue(Task.objects.filter(id=task.id).exists())
        
        # Send PUT request to update the task
        response = self.client.put(f'/tasks/{task.id}/', data=self.UPDATED_TASK_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh task from database
        task.refresh_from_db()

        # Check updated data
        self.assertEqual(task.title, self.UPDATED_TASK_DATA['title'])
        self.assertEqual(task.description, self.UPDATED_TASK_DATA['description'])
        self.assertEqual(task.priority, self.UPDATED_TASK_DATA['priority'])
        self.assertEqual(task.color, self.UPDATED_TASK_DATA['color'])
        self.assertEqual(task.board_column, self.UPDATED_TASK_DATA['board_column'])
    
    
    def test_delete_scrumboard(self):
        task = self.create_task()
        self.assertTrue(Task.objects.filter(id=task.id).exists())
        
        # Delete the task
        response = self.client.delete(f'/tasks/{task.id}/')
        
        # Check if the task is deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())