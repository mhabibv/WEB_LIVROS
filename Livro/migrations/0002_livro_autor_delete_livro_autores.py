# Generated by Django 4.2.11 on 2024-04-14 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Autor', '0002_alter_autor_died_in'),
        ('Livro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Autor.autor'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Livro_Autores',
        ),
    ]
