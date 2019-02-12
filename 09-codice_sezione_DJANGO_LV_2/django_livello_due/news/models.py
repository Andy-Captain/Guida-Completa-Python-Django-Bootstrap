from django.db import models
from django.urls import reverse

# I modelli sono sottoclassi di django.db.models.Model
# I campi dei modelli sono invece definiti in django.db.models.fields
# Campi dei Modelli: https://docs.djangoproject.com/en/2.0/ref/models/fields/
# ForeignKey: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey
# Making Queries: https://docs.djangoproject.com/en/2.0/topics/db/queries/

# Create your models here.

class Giornalista(models.Model):
    """ il modello generico di un giornalista """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        # link utile : https://docs.djangoproject.com/en/2.0/ref/models/options/
        verbose_name = "Giornalista"
        verbose_name_plural = "Giornalisti"


class Articolo(models.Model):
    """ il modello generico di un articolo di news """
    titolo = models.CharField(max_length=100) # alcuni campi necessitano di parametri obbligatori!
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, 
                                    on_delete=models.CASCADE, 
                                    related_name="articoli")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_detail", kwargs={"pk": self.pk})

    class Meta:
        # link utile : https://docs.djangoproject.com/en/2.0/ref/models/options/
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
