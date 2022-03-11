import email
from pyexpat import model
from django.db import models

class Kerdes(models.Model):
    class Meta:        
        verbose_name = 'Kérdés'
        verbose_name_plural = 'Kérdések'

    kerdes = models.CharField(max_length=255)
    helyes = models.CharField(max_length=255)
    rossz1 = models.CharField(max_length=255)
    rossz2 = models.CharField(max_length=255)
    rossz3 = models.CharField(max_length=255)
    szam = models.IntegerField()
    logikai = models.BooleanField()
    valosszam =  models.FloatField()
    hosszuszoveg = models.TextField()
    email = models.EmailField()
    url = models.URLField()
    hulyeseg = models.TextField()

    def __str__(self):
        return f"{self.kerdes}: {self.helyes}"