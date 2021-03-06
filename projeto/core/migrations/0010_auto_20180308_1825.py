# Generated by Django 2.0.3 on 2018-03-08 21:25

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180308_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_edp',
            name='atividades',
        ),
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
            name='player_video',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_edp',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
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
