# Generated by Django 3.2 on 2022-05-24 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_todo_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-id']},
        ),
    ]