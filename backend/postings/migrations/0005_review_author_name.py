# Generated by Django 2.1.1 on 2018-10-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0004_remove_reviewhelpfulvote_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author_name',
            field=models.CharField(default='Anonymous', max_length=64),
        ),
    ]
