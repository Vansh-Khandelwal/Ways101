# Generated by Django 3.2.3 on 2022-12-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0007_remove_user_upvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileImg',
            field=models.IntegerField(default=1),
        ),
    ]
