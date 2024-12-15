# Generated by Django 3.1.14 on 2024-12-15 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20241215_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="Pokemon's id"),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pokemon_entities.pokemon', verbose_name='Previous evolution'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=400, verbose_name='Title in Russian'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(max_length=400, null=True, verbose_name='Title in English'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=400, null=True, verbose_name='Title in Japanese'),
        ),
    ]
