# Generated by Django 2.0.10 on 2019-02-05 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularioscdc', '0007_remove_formulario_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='respuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formularioscdc.RespuestaBinaria'),
        ),
    ]