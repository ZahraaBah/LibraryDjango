# Generated by Django 5.0.7 on 2025-01-16 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_book_borrow_genre_libraryuser_delete_user_book_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='penalty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
