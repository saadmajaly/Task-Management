# Generated by Django 4.2.5 on 2023-12-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_alter_task_taskpriority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
