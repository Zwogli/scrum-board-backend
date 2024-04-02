from django.db import models
import datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from . import choices

def is_due_date_into_future(due_date):
    return due_date < datetime.date.today()

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description= models.TextField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    created_at = models.DateField(default=datetime.date.today)
    due_date = models.DateField()
    
    priority = models.CharField(max_length=7, choices=choices.PRIORITY_CHOICES, default='low')
    color = models.CharField(max_length=23, choices=choices.COLOR_CHOICES, default='#FF0000')
    board_column = models.CharField(max_length=21, choices=choices.BOARD_COLUMN_CHOICES, default='board-column-todo')
    
    def clean(self):
        if is_due_date_into_future(self.due_date):
            raise ValidationError(_('Due date cannot be in the past.'))

    def save(self, *args, **kwargs):
        self.full_clean()  # run clean() method before saving
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'({self.id}) Title: {self.title}, Priority: {self.priority}, Board-column: {self.board_column}'