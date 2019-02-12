from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Autore, Libro

# Create your views here.

class AutoreDetailCBV(DetailView):
    model = Autore
    template_name = "autore.html"


class LibroListCBV(ListView):
    model = Libro
    template_name = "lista_libri.html"
