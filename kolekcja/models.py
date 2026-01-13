from django.db import models

class Film(models.Model):
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    rezyser = models.CharField(max_length=100)
    # null=True i blank=True oznacza, że plakat nie jest obowiązkowy
    plakat = models.ImageField(upload_to='plakaty', null=True, blank=True)

    def __str__(self):
        return self.tytul