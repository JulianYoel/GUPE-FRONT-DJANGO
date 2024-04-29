# Generated by Django 4.2.6 on 2023-11-10 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursada', '0001_initial'),
        ('materia', '0001_initial'),
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursada',
            name='fk_id_materia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cursadas_materia', to='materia.materia'),
        ),
        migrations.AddField(
            model_name='cursada',
            name='fk_id_profesor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cursadas_profesor', to='profesor.profesor'),
        ),
    ]
