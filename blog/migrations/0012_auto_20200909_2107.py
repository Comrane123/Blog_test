# Generated by Django 3.0.7 on 2020-09-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200909_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='post_pics'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
