# Generated by Django 2.0.7 on 2018-09-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]