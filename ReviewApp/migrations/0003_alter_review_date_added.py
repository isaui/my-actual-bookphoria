# Generated by Django 4.2.4 on 2023-10-30 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0002_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]