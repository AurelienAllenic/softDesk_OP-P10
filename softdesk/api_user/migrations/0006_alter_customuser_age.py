# Generated by Django 5.0.2 on 2024-02-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0005_customuser_consent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='age'),
        ),
    ]