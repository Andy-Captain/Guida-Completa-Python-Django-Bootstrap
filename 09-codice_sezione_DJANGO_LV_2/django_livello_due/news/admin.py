from django.contrib import admin

# Register your models here.
from .models import Articolo, Giornalista


admin.site.register(Articolo)
admin.site.register(Giornalista)

# documentazione: https://docs.djangoproject.com/en/2.0/ref/contrib/admin/