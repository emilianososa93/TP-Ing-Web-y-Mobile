# Generated by Django 3.1 on 2020-09-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0005_auto_20200921_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='Nombre',
            field=models.CharField(default='ninguno', max_length=40),
            preserve_default=False,
        ),
    ]
