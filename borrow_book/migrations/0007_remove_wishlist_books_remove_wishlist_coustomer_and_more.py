# Generated by Django 4.2.9 on 2024-04-13 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0006_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='books',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='coustomer',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]