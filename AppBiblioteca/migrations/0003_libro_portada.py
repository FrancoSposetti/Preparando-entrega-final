# Generated by Django 5.0.6 on 2024-08-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBiblioteca', '0002_alquiler_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
    ]
