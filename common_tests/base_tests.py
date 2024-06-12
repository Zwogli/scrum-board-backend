
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class BaseTestSetup(TestCase):
    TEST_TASK_DATA = (
    ('id', 1),
    ('title', 'Test'),
    ('description', 'Test description'),
    ('author', 'test_user'),
    ('author_username', 'test_user'),
    ('created_at', '2024-06-12'),
    ('due_date', '2024-06-12'),
    ('priority', 'high'),
    ('color', 'red'),
    ('board_column', 'board-column-todo')
    )
    
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)