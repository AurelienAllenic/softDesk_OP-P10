# Generated by Django 5.0.2 on 2024-02-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0004_remove_customuser_consent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='consent',
            field=models.BooleanField(default=False),
        ),
    ]
