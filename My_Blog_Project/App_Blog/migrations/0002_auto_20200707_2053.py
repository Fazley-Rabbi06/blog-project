# Generated by Django 3.0 on 2020-07-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='blog_image', verbose_name='Image'),
        ),
    ]
