# Generated by Django 3.1.14 on 2024-12-15 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20241214_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Предок покемона'),
        ),
    ]
