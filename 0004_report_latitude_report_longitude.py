# Generated by Django 4.0.5 on 2024-05-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_addrestaurentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='latitude',
            field=models.FloatField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='longitude',
            field=models.FloatField(default=112),
            preserve_default=False,
        ),
    ]
