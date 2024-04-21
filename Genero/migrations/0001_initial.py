# Generated by Django 4.2.11 on 2024-04-13 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Livro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_Genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero_Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Genero.generos')),
                ('Livro_Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Livro.livro')),
            ],
        ),
        migrations.CreateModel(
            name='Genero_Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Genero.generos')),
            ],
        ),
    ]
