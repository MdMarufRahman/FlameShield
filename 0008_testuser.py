# Generated by Django 4.0.5 on 2024-05-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('img', models.TextField()),
            ],
        ),
    ]
