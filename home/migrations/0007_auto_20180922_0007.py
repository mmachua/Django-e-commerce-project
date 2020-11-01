# Generated by Django 2.0.7 on 2018-09-21 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create',
            name='date',
        ),
        migrations.AddField(
            model_name='create',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]