# Generated by Django 3.1 on 2020-09-08 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('FechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('Puntos', models.IntegerField(default=0)),
                ('WeAreLegion', models.BooleanField(default=False)),
                ('PixelOfLife', models.BooleanField(default=False)),
                ('Conectado', models.BooleanField(default=False)),
                ('Baneado', models.BooleanField(default=False)),
            ],
        ),
    ]
