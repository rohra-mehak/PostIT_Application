# Generated by Django 3.2 on 2021-04-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postIt', '0007_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
