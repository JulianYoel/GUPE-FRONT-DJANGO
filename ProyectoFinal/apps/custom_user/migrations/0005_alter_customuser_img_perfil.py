# Generated by Django 5.0.4 on 2024-04-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_remove_customuser_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img_perfil',
            field=models.ImageField(blank=True, default='perfiles/UserProfile.png', null=True, upload_to='perfiles/'),
        ),
    ]
