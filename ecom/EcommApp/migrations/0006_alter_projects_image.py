# Generated by Django 5.1.6 on 2025-03-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0005_projects_alter_services_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='Projects_Images'),
        ),
    ]
