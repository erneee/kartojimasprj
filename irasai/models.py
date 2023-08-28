from django.db import models

# Create your models here.
class Artistas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=100)
    metai = models.IntegerField("Pradejo-metai")
    biografija = models.TextField("Biografija", max_length=2000)

    def __str__(self):
        return self.pavadinimas

class Irasai(models.Model):
    albumas = models.CharField('Albumas', max_length=100)
    metai_pasirode = models.IntegerField("Pirmo leidimo metai")
    aprasymas = models.TextField('Aprasymas', max_length=2000)
    artistasFK = models.ForeignKey('Artistas', on_delete=models.SET_NULL, null=True, related_name='irasas_sukurimas')

    def __str__(self):
        return self.albumas