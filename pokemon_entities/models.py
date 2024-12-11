from django.db import models  # noqa F401

class Pokemon(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images',null=True)
    def __str__(self):
        return '{}'.format(self.title)
    
class PokemonEntity(models.Model):
    Lat = models.FloatField()
    Lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon,on_delete=models.CASCADE,null=True)
    appeared_at = models.DateTimeField(verbose_name='Appeared at',null=True)
    disappeared_at = models.DateTimeField(verbose_name='Disappeared at',null=True)
