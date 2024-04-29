# Generated by Django 4.2.6 on 2023-11-10 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('fk_id_carrera', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='materia_carrera', to='carrera.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Votacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(default=None)),
                ('carrera', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='votaciones_carrera', to='materia.materia')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='votaciones_mat_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]