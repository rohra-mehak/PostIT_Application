# Generated by Django 3.2.2 on 2021-05-10 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postIt', '0011_post_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
