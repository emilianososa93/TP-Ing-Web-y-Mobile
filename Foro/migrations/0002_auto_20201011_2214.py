# Generated by Django 3.1 on 2020-10-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
