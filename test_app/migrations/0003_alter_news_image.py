# Generated by Django 4.2.4 on 2023-09-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_alter_category_options_alter_news_options_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news-image'),
        ),
    ]
