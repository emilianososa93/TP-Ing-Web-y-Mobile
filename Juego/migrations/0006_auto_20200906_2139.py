# Generated by Django 3.1 on 2020-09-07 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0005_auto_20200906_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixel',
            name='lienzo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Juego.lienzo'),
        ),
    ]
