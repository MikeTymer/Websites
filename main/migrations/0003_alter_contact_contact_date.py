# Generated by Django 5.0.1 on 2024-03-03 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_blogcomment_author_blog_views_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]