# Generated by Django 3.2.3 on 2021-06-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date_time',
        ),
    ]