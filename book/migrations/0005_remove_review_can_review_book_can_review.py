# Generated by Django 4.2.9 on 2024-04-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_wishlist_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='can_review',
        ),
        migrations.AddField(
            model_name='book',
            name='can_review',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]