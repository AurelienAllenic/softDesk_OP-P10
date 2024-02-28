# Generated by Django 5.0.2 on 2024-02-27 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0002_rename_project_contributor_project_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_project.contributor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_project.project')),
            ],
            options={
                'unique_together': {('project', 'contributor')},
            },
        ),
    ]
