from django.db import models


class Pokemon(models.Model):
    title = models.CharField(null=True,
                             max_length=400, verbose_name='Наименование на русском')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение')
    description = models.TextField(null=True, verbose_name="Описание")
    title_en = models.CharField(
        max_length=400, null=True, verbose_name='Наименование на английском')
    title_jp = models.CharField(
        max_length=400, null=True, verbose_name='Наименование на японском')
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        verbose_name='Предок покемона',
        related_name='children',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(
        Pokemon, related_name='pokemons', on_delete=models.CASCADE, null=True)
    appeared_at = models.DateTimeField(
        verbose_name='Время появления', null=True)
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения', null=True)
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(
        null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(
        null=True, blank=True, verbose_name='Выносливость')

    def __str__(self):
        pokemon_name = self.pokemon.title
        latitude = self.latitude
        longitude = self.longitude
        return 'Покемон:{} Широта:{} Долгота:{}'.format(pokemon_name, latitude, longitude)
