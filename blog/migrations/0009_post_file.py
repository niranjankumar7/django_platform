# Generated by Django 2.1.2 on 2019-07-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='default.jpg', upload_to=''),
        ),
    ]