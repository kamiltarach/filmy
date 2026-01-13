from django.db import models

class Film(models.Model):
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    rezyser = models.CharField(max_length=100)
    plakat = models.ImageField(upload_to='plakaty', null=True, blank=True)
    ocena = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.tytul