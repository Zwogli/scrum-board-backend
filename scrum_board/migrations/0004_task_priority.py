# Generated by Django 5.0.3 on 2024-03-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum_board', '0003_task_board_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high', 'high'), ('mid', 'mid'), ('low', 'low')], default='low', max_length=7),
        ),
    ]