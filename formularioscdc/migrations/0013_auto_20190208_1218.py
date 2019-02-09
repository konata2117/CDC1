# Generated by Django 2.0.10 on 2019-02-08 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularioscdc', '0012_auto_20190208_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='formulario',
            name='pregunta',
            field=models.ForeignKey(blank=True, limit_choices_to={'comuna': models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formularioscdc.Comuna')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='formularioscdc.Realiza'),
        ),
    ]