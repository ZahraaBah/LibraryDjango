# Generated by Django 5.1.2 on 2025-01-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_users_email_users_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.CharField(default='user', max_length=10),
        ),
    ]
