# Generated by Django 5.0.6 on 2024-06-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rum', '0002_remove_usuario_activo_usuario_apellido_materno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(db_column='idUsuario', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
