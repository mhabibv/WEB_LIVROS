# Generated by Django 4.2.11 on 2024-04-21 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Genero', '0004_genero_autor'),
        ('Autor', '0002_alter_autor_died_in'),
        ('Usuario', '0003_usuario_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='generos_favoritos',
            field=models.ManyToManyField(blank=True, to='Genero.generos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Autor.autor'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
