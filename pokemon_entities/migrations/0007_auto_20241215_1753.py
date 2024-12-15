# Generated by Django 3.1.14 on 2024-12-15 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_pokemon_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pokemon_entities.pokemon', verbose_name='Предок покемона'),
        ),
    ]