# Generated by Django 2.0.10 on 2019-01-17 13:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formularioscdc', '0008_formulario_rol'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Formulario',
            new_name='Formulari',
        ),
    ]
