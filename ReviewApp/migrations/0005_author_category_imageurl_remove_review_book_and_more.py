# Generated by Django 4.2.5 on 2023-10-29 07:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReviewApp', '0004_delete_author_delete_category_delete_imageurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ImageUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('language', models.CharField(max_length=10)),
                ('currencyCode', models.CharField(blank=True, max_length=10, null=True)),
                ('is_ebook', models.BooleanField()),
                ('pdf_available', models.BooleanField()),
                ('pdf_link', models.URLField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('saleability', models.BooleanField(default=False)),
                ('buy_link', models.URLField(blank=True, null=True)),
                ('epub_available', models.BooleanField(default=False)),
                ('epub_link', models.URLField(blank=True, null=True)),
                ('maturity_rating', models.CharField(max_length=25)),
                ('page_count', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('user_publish_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_last_edit_time', models.DateTimeField(blank=True, null=True)),
                ('authors', models.ManyToManyField(related_name='authors_book', to='ReviewApp.author')),
                ('categories', models.ManyToManyField(related_name='book_categories', to='ReviewApp.category')),
                ('images', models.ManyToManyField(to='ReviewApp.imageurl')),
            ],
        ),
    ]