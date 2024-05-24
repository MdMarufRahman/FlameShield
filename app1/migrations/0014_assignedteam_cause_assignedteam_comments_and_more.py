# Generated by Django 5.0.4 on 2024-05-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_assignedteam_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedteam',
            name='cause',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='assignedteam',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignedteam',
            name='damage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='assignedteam',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='assignedteam',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='assignedteam',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]