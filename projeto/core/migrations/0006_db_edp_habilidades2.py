# Generated by Django 2.0.3 on 2018-03-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180305_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_edp',
            name='habilidades2',
            field=models.CharField(choices=[('t', 'tradução'), ('w', 'escrita'), ('r', 'leitura'), ('l', 'escuta'), ('s', 'fala')], max_length=1, null=True),
        ),
    ]
