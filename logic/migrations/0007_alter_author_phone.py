# Generated by Django 5.1 on 2024-08-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
