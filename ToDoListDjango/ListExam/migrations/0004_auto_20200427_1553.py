# Generated by Django 3.0.5 on 2020-04-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListExam', '0003_todo_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(),
        ),
    ]
