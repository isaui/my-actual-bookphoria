# Generated by Django 4.2.6 on 2023-10-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_alter_book_authors_alter_book_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='authors_book', to='Homepage.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='book_categories', to='Homepage.category'),
        ),
    ]