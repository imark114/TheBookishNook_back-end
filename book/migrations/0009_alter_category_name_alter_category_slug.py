# Generated by Django 4.2.9 on 2024-04-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_book_genre_book_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=25),
        ),
    ]
