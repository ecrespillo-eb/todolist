from django.db import migrations
from todolist_app.models import Priority, Todo
from django.contrib.auth.models import User


def create_priorities(*args):
    Priority.objects.bulk_create([
        Priority(description='Low', order=0),
        Priority(description='Normal', order=1),
        Priority(description='Urgent', order=2),
        Priority(description='Super Urgent', order=3),
    ])


def create_users(*args):
    User.objects.bulk_create([
        User(username="test_user_1", email="test@gmail.com", password=1234),
    ])


def create_tasks(*args):
    user = User.objects.first()
    priority = Priority.objects.first()
    Todo.objects.bulk_create([
        Todo(description='test_task_01', done=False, priority=priority, assigned_user=user),
        Todo(description='test_task_02', done=True, priority=priority, assigned_user=user),
        Todo(description='test_task_03', done=False, priority=priority, assigned_user=user),
        Todo(description='test_task_04', done=True, priority=priority, assigned_user=user),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('todolist_app', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_priorities),
        migrations.RunPython(create_users),
        migrations.RunPython(create_tasks),
    ]
