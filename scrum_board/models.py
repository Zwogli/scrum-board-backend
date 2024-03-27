from django.db import models
import datetime
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(default=datetime.date.today)
    due_date = models.DateField()
    PRIORITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )
    
    def task_id(self):
        return self.id