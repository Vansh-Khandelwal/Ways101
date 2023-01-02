# Generated by Django 3.2.3 on 2022-11-16 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymous', max_length=50)),
                ('content', models.CharField(default='', max_length=500)),
                ('date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]
