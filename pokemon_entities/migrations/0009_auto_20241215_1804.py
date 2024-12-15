# Generated by Django 3.1.14 on 2024-12-15 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20241215_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pokemon_entities.pokemon', verbose_name='Предок покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=400, verbose_name='Наименование на русском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(max_length=400, null=True, verbose_name='Наименование на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=400, null=True, verbose_name='Наименование на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(null=True, verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(verbose_name='Броня'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(null=True, verbose_name='Время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(verbose_name='Сила'),
        ),
    ]
