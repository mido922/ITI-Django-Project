# Generated by Django 4.2.10 on 2024-02-19 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
