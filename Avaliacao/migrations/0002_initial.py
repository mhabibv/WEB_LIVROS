# Generated by Django 4.2.11 on 2024-04-13 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Avaliacao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Livro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='usuario_comentando',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='livro_avaliado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Livro.livro'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='usuario_avaliando',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
