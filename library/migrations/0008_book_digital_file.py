# Generated by Django 5.0.3 on 2025-01-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_useractivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='digital_file',
            field=models.FileField(blank=True, null=True, upload_to='book_files/'),
        ),
    ]
