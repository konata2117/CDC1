# Generated by Django 2.0.10 on 2019-01-30 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularioscdc', '0010_auto_20190130_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParaPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formularioscdc.Formulario')),
            ],
        ),
    ]