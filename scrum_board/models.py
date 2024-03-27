from django.db import models
import datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
        ('high', 'high'),
        ('mid', 'mid'),
        ('low', 'low'),
    )
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default='low')
    
    COLOR_CHOICES = (
        ('#FF0000', 'Red'),
        ('#00FF00', 'Green'),
        ('#0000FF', 'Blue'),
        ('#FFFF00', 'Yellow'),
        ('#FF00FF', 'Magenta'),
        ('#00FFFF', 'Cyan'),
        # Weitere Farben nach Bedarf hinzufügen
    )
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#FF0000')
    
    BOARD_COLUMN_CHOICES = (
        ('board-column-todo', 'board-column-todo'),
        ('board-column-progress', 'board-column-progress'),
        ('board-column-feedback', 'board-column-feedback'),
        ('board-column-done', 'board-column-done')
    )
    board_column = models.CharField(max_length=21, choices=BOARD_COLUMN_CHOICES, default='board-column-todo')
    
    
    def task_id(self):
        return self.id
    
    def clean(self):
        if self.due_date < datetime.date.today():
            raise ValidationError(_('Due date cannot be in the past.'))

    def save(self, *args, **kwargs):
        self.full_clean()  # run clean() method before saving
        super().save(*args, **kwargs)