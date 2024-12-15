from django.db import models  # noqa F401


class Pokemon(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, verbose_name="Идентификатор")
    title = models.CharField(
        max_length=400, verbose_name='Наименование на русском')
    image = models.ImageField(null=True, verbose_name='Изображение')
    description = models.TextField(null=True, verbose_name="Описание")
    title_en = models.CharField(
        max_length=400, null=True, verbose_name='Наименование на английском')
    title_jp = models.CharField(
        max_length=400, null=True, verbose_name='Наименование на японском')
    parent = models.ForeignKey(
        'self', null=True,
        verbose_name='Предок покемона',
        related_name='children',
        on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
    appeared_at = models.DateTimeField(
        verbose_name='Время появления', null=True)
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения', null=True)
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    strength = models.IntegerField(verbose_name='Сила')
    defence = models.IntegerField(verbose_name='Броня')
    stamina = models.IntegerField(verbose_name='Выносливость')
