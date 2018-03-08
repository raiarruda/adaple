# Generated by Django 2.0.3 on 2018-03-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180308_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_edp',
            name='anotacao_texto',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='carregar_audio',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='carregar_imagem',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='carregar_video',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='player_audio',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='player_imagem',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
