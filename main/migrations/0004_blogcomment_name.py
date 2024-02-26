# Generated by Django 4.0.6 on 2024-02-13 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Write your full name here', max_length=30),
            preserve_default=False,
        ),
    ]
