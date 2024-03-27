# Generated by Django 5.0.3 on 2024-03-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(choices=[('#FF0000', 'Red'), ('#00FF00', 'Green'), ('#0000FF', 'Blue'), ('#FFFF00', 'Yellow'), ('#FF00FF', 'Magenta'), ('#00FFFF', 'Cyan')], default='#FF0000', max_length=7),
        ),
    ]
