# Generated by Django 4.1 on 2022-08-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default='Deneme', max_length=50),
        ),
    ]