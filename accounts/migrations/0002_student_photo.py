# Generated by Django 4.2.3 on 2023-07-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='profile_photos'),
        ),
    ]
