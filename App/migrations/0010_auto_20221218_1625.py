# Generated by Django 3.2.3 on 2022-12-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_way_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='way',
            name='downvotes',
        ),
        migrations.AddField(
            model_name='way',
            name='downvotes',
            field=models.TextField(default=''),
        ),
    ]