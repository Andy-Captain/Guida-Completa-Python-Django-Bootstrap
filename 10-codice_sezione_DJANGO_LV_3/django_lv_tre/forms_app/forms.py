# importiamo forms in modo da poter creare una classe figlia e utilizzarne le funzioni
# https://docs.djangoproject.com/en/2.0/topics/forms/#the-django-form-class

from django import forms

# Documentazione sui campi utilizzabili con Form e Parametri: https://docs.djangoproject.com/en/2.0/ref/forms/fields/

# class FormContatto(forms.Form):
#     nome = forms.CharField(required)
#     cognome = forms.CharField()
#     email = forms.EmailField()
#     contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!"}))

from django.core import validators
from django.core.exceptions import ValidationError

# DOCUMENTAZIONE UTILE:
# BUILT-IN VALIDATORS:  https://docs.djangoproject.com/en/2.0/ref/validators/
# LINK VALIDAZIONE:     https://docs.djangoproject.com/en/2.0/ref/forms/validation/
# FORM API:             https://docs.djangoproject.com/en/2.0/ref/forms/api/
# WORKING WITH FORMS:   https://docs.djangoproject.com/en/2.0/topics/forms/

class FormContatto(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control"}))
    cognome = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control"}))
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={"class": "form-control"}))
    contenuto = forms.CharField(
        widget=forms.Textarea(
        attrs={"placeholder": "Area Testuale! Scrivi pure!", "class": "form-control"}),
        validators=[validators.MinLengthValidator(10)])

    def clean_contenuto(self):
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viole le norme del sito!")
        return dati
