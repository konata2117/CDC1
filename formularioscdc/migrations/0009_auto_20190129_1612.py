# Generated by Django 2.0.10 on 2019-01-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioscdc', '0008_auto_20190129_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='pregunta',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]