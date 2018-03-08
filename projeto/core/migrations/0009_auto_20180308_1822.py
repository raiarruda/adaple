# Generated by Django 2.0.3 on 2018-03-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180308_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_edp',
            name='anotacao_texto',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='carregar_audio',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='carregar_imagem',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='carregar_video',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='player_audio',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='player_imagem',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='player_video',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='texto',
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='video',
        ),
        migrations.AddField(
            model_name='db_edp',
            name='atividades',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='db_edp',
            name='habilidades',
        ),
        migrations.AddField(
            model_name='db_edp',
            name='habilidades',
            field=models.ManyToManyField(to='core.db_habilidades'),
        ),
    ]
