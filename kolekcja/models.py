from django.db import models

class Film(models.Model):
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    rezyser = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tytul