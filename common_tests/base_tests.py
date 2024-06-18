
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from scrum_board.models import Task
from datetime import date, timedelta

class BaseTestSetup(TestCase):
    TEST_TASK_DATA = {
        'id': 1,
        'title': 'Test',
        'description': 'Test description',
        'author': 'test_user',
        'author_username': 'test_user',
        'created_at': '2024-06-12',
        'due_date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
        'priority': 'high',
        'color': 'red',
        'board_column': 'board-column-todo'
    }


    UPDATED_TASK_DATA = {
        'title': 'Updated Task',
        'description': 'Updated description',
        'priority': 'low',
        'color': 'blue',
        'board_column': 'board-column-done'
    }
        
        
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        
    def create_task(self):
        task_data = self.TEST_TASK_DATA.copy()
        task_data['author'] = self.user
        task = Task.objects.create(**task_data)
        return task
        
        
    
    