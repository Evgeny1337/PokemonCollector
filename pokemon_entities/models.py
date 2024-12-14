from django.db import models  # noqa F401


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=400)
    image = models.ImageField(null=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Lat')
    longitude = models.FloatField(verbose_name='Lon')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
    appeared_at = models.DateTimeField(verbose_name='Appeared at', null=True)
    disappeared_at = models.DateTimeField(
        verbose_name='Disappeared at', null=True)
    level = models.IntegerField(verbose_name='Level')
    health = models.IntegerField(verbose_name='health')
    strength = models.IntegerField(verbose_name='Strength')
    defence = models.IntegerField(verbose_name='Defence')
    stamina = models.IntegerField(verbose_name='Stamina')
