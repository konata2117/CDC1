# Generated by Django 2.0.10 on 2019-02-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioscdc', '0005_formulario_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='estado_formulario',
            field=models.CharField(blank=True, choices=[('FINALIZADO', 'FINALIZADO'), ('EN PROCESO', 'EN PROCESO')], max_length=30, null=True),
        ),
    ]