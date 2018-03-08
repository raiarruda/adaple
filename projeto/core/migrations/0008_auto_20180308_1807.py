# Generated by Django 2.0.3 on 2018-03-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180308_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_edp',
            name='habilidades',
        ),
        migrations.AddField(
            model_name='db_edp',
            name='habilidades',
            field=models.CharField(choices=[('t', 'tradução'), ('w', 'escrita'), ('r', 'leitura'), ('l', 'escuta'), ('s', 'fala')], max_length=1, null=True),
        ),
    ]
