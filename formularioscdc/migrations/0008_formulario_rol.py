# Generated by Django 2.0.10 on 2019-01-17 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularioscdc', '0007_auto_20190117_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formularioscdc.Rol'),
        ),
    ]