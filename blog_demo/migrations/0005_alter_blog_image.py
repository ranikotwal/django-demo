# Generated by Django 4.2.3 on 2023-07-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_demo', '0004_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
