# Generated by Django 4.2.9 on 2024-02-11 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='012xxxxxxxx', max_length=100)),
                ('birthDate', models.DateField(default=django.utils.timezone.now)),
                ('faceBookAccount', models.URLField(default='https://example.com')),
                ('country', models.CharField(default='Country', max_length=255)),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
